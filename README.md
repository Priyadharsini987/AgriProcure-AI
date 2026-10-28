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

**Model storage:** The three small model files are already present in the repository's root-level `models/` directory. The three large trained model binaries are kept out of Git because of their size and should be downloaded from the configured Hugging Face model repository. The backend now looks in `models/` for all six files and downloads a missing file from Hugging Face when configured.

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
├── models/                 # Existing model package and .joblib artifacts
├── src/                    # React application source
├── public/                 # Static frontend assets
├── package.json
├── vite.config.js
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

### 5. Configure the ML model files

The three small `.joblib` files already in `models/` should remain there. The three large files are:

- `eta_prediction_model.joblib`
- `overload_prediction_model.joblib`
- `demand_forecasting_model.joblib`

Upload those original files to your Hugging Face model repository, keeping their filenames unchanged. Then set the following in your local `.env`:

```dotenv
ML_MODELS_DIR=models
HF_MODEL_REPO=your-username/agriprocure-ml-models
HF_TOKEN=
```

For a public Hugging Face repository, leave `HF_TOKEN` blank. For a private repository, set a Hugging Face read token locally and never commit it. When a local model file is missing, the backend downloads the matching filename from the configured Hugging Face repository. The backend prefers a valid local file first.

The model binaries are intentionally excluded from Git because of their size. Do not create empty placeholder files or rename a different model to match these filenames.

### 6. Start the application

**Windows one-click startup**

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

- Do not commit `.env`, database files, API credentials, or large trained model binaries.
- `.env.example` contains placeholders only; configure real credentials locally.
- The current authentication routes include demo-oriented OTP/Aadhaar verification behaviour. These are **not production identity-verification integrations** and must be replaced with verified provider integrations before real-world use.
- Use a strong, private `SECRET_KEY`; do not use a public/demo key in a deployed environment.
- Review payment, SMS, and WhatsApp provider configuration before enabling live transactions or messages.

## Current ML Artifact Status

The three small model files are stored in GitHub under `models/`. The three large trained model binaries must be supplied through the configured Hugging Face repository (or placed locally in `models/`). Some ML service methods provide fallback or rule-based behaviour when an artifact is unavailable. Therefore, do not describe every prediction as trained-model inference unless the corresponding artifact is present and successfully loaded.

## Future Enhancements
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
