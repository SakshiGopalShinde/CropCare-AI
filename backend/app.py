from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.efficientnet import preprocess_input
import os
import uuid
import logging
import json
import time

# ----------------------------------------
# Quiet TensorFlow Warnings
# ----------------------------------------
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# ----------------------------------------
# Logging Setup
# ----------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cropcare-backend")

# ----------------------------------------
# Flask Setup
# ----------------------------------------
app = Flask(__name__)
CORS(app)

# ----------------------------------------
# Uploads Folder
# ----------------------------------------
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "gif", "tiff"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ----------------------------------------
# Load Model
# ----------------------------------------
MODEL_PATH = r"D:\CropCareAI-main\backend\model\best_efficientnet_model.keras"
logger.info(f"📌 Loading model from: {MODEL_PATH}")

try:
    model = load_model(MODEL_PATH, compile=False)
    logger.info("✅ Model loaded successfully.")
except Exception as e:
    logger.error(f"❌ Model load error: {e}")
    raise


# ----------------------------------------
# Class Names (same order as training)
# ----------------------------------------
class_names = [
    "Aphid", "Brown Rust", "Healthy", "Leaf Blight",
    "Mildew", "Mite", "Septoria", "Smut", "Yellow Rust"
]

# ----------------------------------------
# Load Disease JSON
# ----------------------------------------
DATA_PATH = os.path.join("data", "disease_data.json")

try:
    with open(DATA_PATH, "r") as f:
        disease_info = json.load(f)
    logger.info("📘 Disease JSON loaded.")
except Exception as e:
    logger.error(f"❌ Failed to load disease JSON: {e}")
    disease_info = {}


# ----------------------------------------
# Home Page (optional for browser)
# ----------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------
# API: Prediction for Flutter
# ----------------------------------------
@app.route("/api/predict", methods=["POST"])
def predict_api():
    logger.info("🔵 API /api/predict called")

    # Debug logs for Flutter request
    logger.info(f"Incoming request.files: {request.files}")

    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    # Unique File Save Path
    original = secure_filename(file.filename)
    ext = os.path.splitext(original)[1]
    unique_name = f"{uuid.uuid4().hex}_{int(time.time())}{ext}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)

    # Save file
    file.save(filepath)
    logger.info(f"📁 Saved file to: {filepath}")

    # Process prediction
    return run_prediction(filepath)


# ----------------------------------------
# Prediction Processing Logic
# ----------------------------------------
def run_prediction(filepath: str):
    try:
        # Read and preprocess image
        img = load_img(filepath, target_size=(256, 256))
        img_arr = img_to_array(img)
        img_arr = preprocess_input(img_arr)
        img_arr = tf.expand_dims(tf.convert_to_tensor(img_arr, dtype=tf.float32), axis=0)

        prediction = model.predict(img_arr)

        # If tuple returned (some models do that)
        if isinstance(prediction, (tuple, list)):
            prediction = prediction[0]

        idx = int(tf.argmax(prediction, axis=1)[0])
        label = class_names[idx]
        confidence = round(float(prediction[0][idx]) * 100, 2)

        # URL for Flutter (full http://ip:5000/... path)
        img_url = f"{request.host_url.rstrip('/')}/static/uploads/{os.path.basename(filepath)}"

        solution = disease_info.get(label, {"message": "No data available"})

        # Final JSON response to Flutter
        return jsonify({
            "prediction": label,
            "confidence": confidence,
            "image_url": img_url,
            "solution": solution
        })

    except Exception as e:
        logger.exception("Prediction Error")
        return jsonify({"error": str(e)}), 500


# ----------------------------------------
# Run Server
# ----------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
