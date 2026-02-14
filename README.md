# 🌾 KrishiCare — Smart Crop Disease Detection Platform

### AI‑Powered Crop Health Monitoring | Built for Smart India Hackathon

🔗 Live Demo: [https://cropcareai-u7co.onrender.com/](https://cropcareai-u7co.onrender.com/)

---

## ⚠️ Disclaimer

This project was primarily developed and tested locally during the hackathon and research phase. Some commits, dataset uploads, and documentation updates were pushed later for repository completeness and reproducibility.

---

## About the Project

**KrishiCare (Kisan Rakshak)** is an end‑to‑end AI‑powered crop health monitoring system designed to detect plant diseases early using deep learning. Farmers can upload crop images and receive instant disease predictions along with actionable recommendations.

The solution integrates computer vision models, scalable backend APIs, and a responsive Flutter Web interface to deliver real‑time agricultural decision support.

### Key Objectives

* Early disease detection to reduce crop loss
* Improve yield through timely intervention
* Provide accessible AI tools for farmers
* Enable scalable agricultural monitoring

---

## Key Capabilities

### AI‑Based Crop Disease Detection

* Upload crop or leaf images from smartphone
* Detect disease type and severity
* Confidence‑scored predictions using CNN models (EfficientNet, ResNet)

### Remote Crop Health Monitoring

* Drone + satellite NDVI monitoring
* Detect stress zones in large farms
* Predict potential outbreak areas

### Geo‑Mapping & Risk Alerts

* GIS‑based disease hotspot mapping
* Real‑time alerts to nearby farmers
* Prevent rapid disease spread

### Actionable Agronomy Guidance

* Localized treatment recommendations
* Preventive measures based on crop stage
* Weather‑aware intervention planning

### National Recognition

**Kisan Rakshak** was selected as a winning solution at **Smart India Hackathon 2025**, validating its innovation, feasibility, and real‑world impact.

---

## 🧠 Image Segmentation & Patch Generation Pipeline

### Patch Extraction from Leaf Images

![Patch Extraction](https://github.com/SakshiGopalShinde/cropcare/raw/main/test_images/Screenshot%202026-02-14%20203158.png)
Direct image link: [https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20203158.png](https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20203158.png)

Process overview:

* Sample dataset images are analyzed and infected regions are localized
* Disease‑affected leaf portions are isolated
* Image patches are generated and passed to the prediction model

---

### UNet Segmentation Workflow

![Segmentation Pipeline](https://github.com/SakshiGopalShinde/cropcare/raw/main/test_images/Screenshot%202026-02-14%20203214.png)
Direct image link: [https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20203214.png](https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20203214.png)

Pipeline Steps:

1. Input images are downsampled for efficient computation
2. Adaptive + grid patch generation modules create focused training samples
3. Patch‑level data augmentation improves generalization
4. Adaptive patches train a UNet segmentation network
5. Grid patch predictions generate masks that feed back into the adaptive module

---

## 🏗️ System Architecture & Workflow

![System Architecture](https://github.com/SakshiGopalShinde/cropcare/raw/main/test_images/Screenshot%202026-02-14%20204019.png)
Direct architecture link: [https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20204019.png](https://github.com/SakshiGopalShinde/cropcare/blob/main/test_images/Screenshot%202026-02-14%20204019.png)

### End‑to‑End Workflow

1. Data Sources → Farmer images, historical datasets, and weather APIs
2. Preprocessing → Cleaning, resizing, augmentation, dataset splitting
3. Model Training → CNN models (EfficientNet / ResNet) trained on augmented data
4. Segmentation Module → UNet identifies infected regions
5. Model Optimization → Quantization and TensorFlow Lite deployment
6. Backend API → FastAPI/TensorFlow Serving handles predictions
7. Frontend → Flutter Web interface for farmers
8. Cloud Storage → Model hosting and data logging
9. Communication Layer → Risk visualization, alerts, and periodic reports

This modular architecture ensures scalability, faster inference, and real‑world deployment readiness.

---

![System Architecture](https://github.com/SakshiGopalShinde/cropcare/raw/main/test_images/Screenshot%202026-02-14%20204019.png)

### End‑to‑End Workflow

1. **Data Sources** → Farmer images, historical datasets, and weather APIs
2. **Preprocessing** → Cleaning, resizing, augmentation, dataset splitting
3. **Model Training** → CNN models (EfficientNet / ResNet) trained on augmented data
4. **Segmentation Module** → UNet identifies infected regions
5. **Model Optimization** → Quantization and TensorFlow Lite deployment
6. **Backend API** → FastAPI/TensorFlow Serving handles predictions
7. **Frontend** → Flutter Web interface for farmers
8. **Cloud Storage** → Model hosting and data logging
9. **Communication Layer** → Risk visualization, alerts, and periodic reports

This modular architecture ensures scalability, faster inference, and real‑world deployment readiness.

---

## Tech Stack

Frontend: Flutter Web
Backend API: Python / FastAPI / Flask
ML Models: TensorFlow / PyTorch
Segmentation: UNet
Model Optimization: TensorFlow Lite + Quantization
Hosting: Render
Storage: Firebase / Cloudinary / Cloud Storage

---

## Project Structure

lib/
│── main.dart
├── screens/home_screen.dart
├── widgets/upload_card.dart
└── services/api_service.dart

assets/
web/
test_images/

---

## How It Works

User uploads crop image → Flutter Web sends image to ML API → Segmentation + CNN model processes image → Prediction + confidence score returned → Results displayed with guidance

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

* More crop disease datasets
* Offline prediction support
* Android & iOS mobile apps
* Multilingual farmer advisory
* Integration with IoT soil sensors

---

If you found this project useful, please consider starring the repository.
