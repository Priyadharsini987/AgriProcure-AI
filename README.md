# 🌾 AgriProcure AI
### AI-Powered Smart Agricultural Procurement Platform

AgriProcure AI is a full-stack agricultural procurement platform designed to improve coordination between farmers and procurement officers. It combines a React frontend, Flask REST API, SQL database integration, and six machine-learning components for procurement planning and operational decision support.

## Key Features

### Farmer Portal
- Farmer registration and login
- Crop declaration with acreage and expected quantity
- Procurement-centre recommendations
- Smart time-slot allocation
- Digital booking tokens and QR codes
- Queue position and estimated waiting-time tracking
- Procurement progress and payment-status tracking

### Procurement Officer Dashboard
- Procurement-centre and queue monitoring
- Demand forecasting and overload-risk analysis
- Operational decision support
- Farmer reallocation recommendations
- What-if simulations through a digital-twin service

### Six ML Components

| Model artifact | Purpose |
|---|---|
| `centre_recommendation_model.joblib` | Procurement-centre recommendation |
| `demand_forecasting_model.joblib` | Crop-arrival demand forecasting |
| `eta_prediction_model.joblib` | Waiting-time estimation |
| `officer_decision_intelligence_model.joblib` | Officer decision support |
| `overload_prediction_model.joblib` | Procurement-centre overload prediction |
| `smart_slot_allocation_model.joblib` | Delivery time-slot allocation |

**Important:** The trained `.joblib` binaries are not included in this source repository. The ML service contains model-loading logic and fallback behaviour for some components, but fallback output is not the same as inference from the trained artifact. To use trained predictions, obtain all six original files and place them in the `ml_artifacts/` directory described below.

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React 19, Vite, Tailwind CSS |
| Backend | Python, Flask, Flask REST APIs |
| Database / ORM | SQLite by default, SQLAlchemy; PostgreSQL/MySQL URL support |
| Machine Learning | Scikit-learn, Pandas, NumPy, Joblib |
| Charts | Recharts |
| Integrations | Razorpay configuration, QR codes, WhatsApp/SMS service hooks |
| Tools | Git, GitHub, VS Code |

## Repository Structure

This repository uses a **single root-level frontend and backend**, not separate `frontend/` and `backend/` folders.

```text
AgriProcure-AI/
├── app.py
├── run.py
├── config.py
├── database.py
├── requirements.txt
├── routes/                 # Flask API blueprints
├── services/               # ML and integration services
├── models/                 # SQLAlchemy database models
├── src/                    # React application source
├── public/                 # Static frontend assets
├── package.json
├── vite.config.js
├── ml_artifacts/           # Local trained .joblib files (not committed)
├── .env.example
├── .gitignore
├── start_app.bat
└── start_app.ps1
```

## Setup and Run Locally

### Prerequisites
- Python 3.11 or compatible version
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Priyadharsini987/AgriProcure-AI.git
cd AgriProcure-AI
```

### 2. Configure environment variables

Create your local environment file from the example:

**Windows PowerShell**
```powershell
Copy-Item .env.example .env
```

Edit `.env` and set a unique `SECRET_KEY`. Add database or third-party credentials only if you use those integrations. The default database is SQLite.

### 3. Install backend dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install frontend dependencies

Run from the repository root:

```bash
npm install
```

### 5. Add trained ML artifacts (if available)

Create the model directory:

```powershell
New-Item -ItemType Directory -Force ml_artifacts
```

Place the six original files listed in the ML table into `ml_artifacts/`. By default, the backend reads from this directory. If you store the files elsewhere, set `ML_MODELS_DIR` in your local `.env` to that directory.

The model files are intentionally ignored by Git because of their size. To download missing artifacts automatically, set `HF_MODEL_REPO` in `.env` to your Hugging Face repository ID (for example, `your-username/agriprocure-ml-models`). The backend prefers a valid local file and otherwise downloads the matching filename from that repository using `huggingface_hub`. For a public model repository, leave `HF_TOKEN` blank. For a private repository, set a Hugging Face read token in your local `.env`. Do not commit that token. Do not create empty placeholder files or rename a different model to match these filenames.

### 6. Start the application

**Windows one-click startup**

After installing both sets of dependencies:

```bat
start_app.bat
```

Or start the backend and frontend in separate terminals from the repository root.

Terminal 1 — Flask backend:
```bash
python run.py
```

Terminal 2 — Vite frontend:
```bash
npm run dev
```

### 7. Open the application

| Component | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend root / health response | http://127.0.0.1:5000/ |

The Vite development server proxies `/api` requests to the Flask server on port 5000.

## Application Workflow

1. Farmers register and submit crop details.
2. The backend processes booking and procurement-centre information.
3. ML services provide recommendations, forecasts, ETA estimates, and overload analysis when their trained artifacts are available.
4. The system creates a booking token and QR code.
5. Farmers can follow queue and procurement progress.
6. Officers monitor centres and can use decision-support and simulation features.

## Configuration and Security Notes

- Do not commit `.env`, database files, API credentials, or trained model binaries.
- `.env.example` contains placeholders only; configure real credentials locally.
- The current authentication routes include demo-oriented OTP/Aadhaar verification behaviour. These are **not production identity-verification integrations** and must be replaced with verified provider integrations before real-world use.
- Use a strong, private `SECRET_KEY`; do not use a public/demo key in a deployed environment.
- Review payment, SMS, and WhatsApp provider configuration before enabling live transactions or messages.

## Current ML Artifact Status

The source code expects six trained model files, but the model binaries are not stored in this GitHub repository. Some ML service methods provide fallback or rule-based behaviour when an artifact is unavailable. Therefore, do not describe every prediction as trained-model inference unless the corresponding artifact is present and successfully loaded.

## Future Enhancements
- Automated secure model-artifact download from a configured model registry
- Production-grade OTP and identity verification
- Improved monitoring, tests, and deployment configuration
- Additional analytics and multilingual support

## Project Information

**Project:** AgriProcure AI  
**Domain:** Artificial Intelligence, Machine Learning, and Full-Stack Development  
**Application Area:** Agricultural Technology

**GitHub:** https://github.com/Priyadharsini987/AgriProcure-AI

---
⭐ If you find this project useful, consider giving the repository a star.
