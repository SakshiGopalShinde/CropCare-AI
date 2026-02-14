# 🌾 KrishiCare -- Smart Crop Disease Detection

### AI-Powered Crop Health Monitoring | Built for Smart India Hackathon

🔗 Live Demo: [https://cropcareai-u7co.onrender.com/](https://cropcareai-u7co.onrender.com/)

---

## About the Project

KrishiCare is an AI-powered crop health monitoring web application built using Flutter Web. It allows farmers to upload crop images and instantly detect plant diseases using trained deep-learning models.

The goal is to provide early disease detection, improve crop yield, and support farmers with accessible technology.

---

## Features

AI-Based Crop Disease Detection

* Upload crop / leaf images
* Detect possible plant diseases
* Display disease name + confidence score

Deep Learning Integration

* Backend ML API for predictions
* Supports multiple crops (wheat, rice, maize, etc.)
* Uses trained CNN models

Built With Flutter Web

* Clean and modern UI
* Fully responsive across devices
* Runs directly in browser

Hosted on Render

* Stable hosting
* Fast and lightweight deployment
* Optimized for Flutter Web

---

## 🧠 Image Segmentation & Patch Generation Pipeline

To improve disease detection accuracy, KrishiCare uses an advanced segmentation-based pipeline that focuses on infected regions of crop leaves before prediction.

### 1️⃣ Patch Extraction from Leaf Images

The system first identifies important regions of the image and extracts smaller patches that contain disease patterns.

![Patch Extraction](Screenshot 2026-02-14 203158.png)

Explanation of the process:

* **(a)** Sample images from the dataset, where red boxes highlight rust-infected regions.
* **(b)** Selected portion of the leaf containing disease-affected areas.
* **(c)** Final image patches generated from the sample image. These patches are fed into the model for prediction.

This helps the model focus only on meaningful disease regions instead of the full background image.

---

### 2️⃣ UNet Segmentation Workflow

KrishiCare uses a UNet-based segmentation pipeline to improve prediction quality and localize disease spots.

![Segmentation Pipeline](Screenshot 2026-02-14 203214.png)

Pipeline Steps:

1. **Downsampling** → Input images are resized to reduce computational load.
2. **Patch Generation** → Includes both adaptive patching and grid patching modules.
3. **Data Augmentation** → Patch-level augmentation improves model robustness.
4. **Training** → Adaptive patches are fed into the UNet segmentation model to learn disease patterns.
5. **Forward Pass + Feedback** → Grid patches generate segmentation masks, which are sent back to the adaptive patch module as feedback for improved learning.

This segmentation approach ensures the model detects diseases more accurately, even in complex backgrounds.

---

## Project Structure

lib/
│── main.dart
├── screens/home_screen.dart
├── widgets/upload_card.dart
└── services/api_service.dart

assets/
web/

---

## How It Works

User uploads crop image → Flutter Web sends image to ML API → API processes image using trained model → Prediction + confidence score returned → Results displayed to the user

---

## Tech Stack

Frontend: Flutter Web
Backend API: Python / FastAPI / Flask
ML Models: TensorFlow / PyTorch
Hosting: Render
Storage: Firebase / Cloudinary / Local Server

---

## Run Locally

```bash
git clone https://github.com/your-username/krishicare.git
cd krishicare
flutter pub get
flutter config --enable-web
flutter run -d chrome
```

---

## Deployment

flutter build web
Upload /build/web to Render Static Site.

---

## Future Improvements

* More crop disease models
* Offline prediction support
* Farmer language support
* Android & iOS mobile apps
* Crop treatment recommendations

---

If you like this project, please star the repo.
