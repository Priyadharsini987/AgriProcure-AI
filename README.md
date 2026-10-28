# 🌾 AgriProcure AI
### AI-Powered Smart Agricultural Procurement Platform

AgriProcure AI is an intelligent agricultural procurement platform designed to modernize crop procurement operations and improve coordination between farmers and procurement officers.

The platform integrates full-stack web development, machine learning, and digital technologies to simplify crop booking, optimize procurement centre allocation, reduce waiting times, and provide data-driven operational insights.

## 🚀 Key Features

### 👨‍🌾 Farmer Portal
- Farmer registration and authentication.
- Crop declaration with acreage and expected quantity.
- AI-powered procurement centre recommendations.
- Smart time-slot allocation.
- Digital token generation with QR codes.
- Queue position and estimated waiting-time tracking.
- Procurement progress monitoring.
- Payment status tracking and notifications.

### 🏢 Procurement Officer Dashboard
- Centralized procurement management.
- Live queue and procurement centre monitoring.
- Crop arrival and demand forecasting.
- Congestion and overload prediction.
- Operational decision support.
- Dynamic farmer allocation across procurement centres.
- What-if simulations for procurement planning.

### 🤖 Machine Learning Integration

The application incorporates six machine learning components:

| Model | Functionality |
|---|---|
| Centre Recommendation | Recommends suitable procurement centres based on operational factors |
| Smart Slot Allocation | Suggests suitable crop delivery time slots |
| ETA Prediction | Estimates farmer waiting time |
| Overload Prediction | Identifies procurement centre congestion |
| Demand Forecasting | Predicts upcoming crop arrivals |
| Officer Decision Intelligence | Supports procurement officers with operational recommendations |

### ⚠️ Trained ML Model Files

**The trained model files are intentionally not uploaded to this GitHub repository because their file sizes are too large.** The source code, ML service integration, and model-loading logic are included, but the trained model binaries must be obtained separately to run the corresponding trained prediction features.

The application expects these six Joblib model files:
- centre_recommendation_model.joblib
- demand_forecasting_model.joblib
- eta_prediction_model.joblib
- officer_decision_intelligence_model.joblib
- overload_prediction_model.joblib
- smart_slot_allocation_model.joblib

The expected file paths are defined in config.py. Place the model files at the configured paths before running trained ML inference. Without these files, trained-model predictions will not be available; individual features may use their implemented fallback behavior where supported.

These artifacts are excluded from the repository to keep the GitHub source repository lightweight.
## 💳 Digital Integrations
- Razorpay payment gateway integration.
- QR code generation for digital tokens.
- WhatsApp click-to-chat notifications.
- WhatsApp Cloud API integration support.
- SMS notification functionality.
- Database integration for procurement records.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | React 19, Vite, Tailwind CSS |
| Backend | Python, Flask, REST APIs |
| Database | SQLite, PostgreSQL |
| ORM | SQLAlchemy |
| Machine Learning | Scikit-learn, Pandas, NumPy |
| Model Serialization | Joblib |
| Data Visualization | Recharts |
| Payment Integration | Razorpay |
| Communication | WhatsApp, SMS |
| Development Tools | Git, GitHub, VS Code |

## 🏗️ System Architecture

```text
          Farmers & Procurement Officers
                       |
                       v
              React 19 + Vite
                 Frontend
                       |
                       v
                Flask REST API
                       |
          +------------+------------+
          |            |            |
          v            v            v
      Machine      Database     External
      Learning     SQLAlchemy   Integrations
      Models         ORM        Razorpay
          |            |         WhatsApp
          |            |         QR / SMS
          +------------+------------+
                       |
                       v
             Agricultural Procurement
                    Platform
```

## 🔄 Application Workflow

1. **User Registration:** Farmers and procurement officers access their respective portals.
2. **Crop Declaration:** Farmers submit crop details, acreage, and expected quantities.
3. **AI Recommendations:** The system recommends suitable procurement centres.
4. **Smart Slot Allocation:** An appropriate delivery time slot is suggested.
5. **Digital Booking:** A procurement token and QR code are generated.
6. **Gate Check-in:** Farmers check in at the procurement centre using their QR code.
7. **Queue Monitoring:** Farmers track their queue position and estimated waiting time.
8. **Procurement Processing:** Crop inspection, quality grading, weighing, and payment stages are tracked.
9. **Officer Management:** Officers monitor procurement operations and use forecasting and decision-support features.

## ⚡ Getting Started

### Prerequisites

- Python 3.11 or compatible version
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Priyadharsini987/AgriProcure-AI.git
cd AgriProcure-AI
```

### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create the required environment configuration using the provided `.env.example` file.

Configure database credentials and external API keys where required.

**Note:** Never commit sensitive credentials, API keys, or passwords to GitHub.

### 4. Run the Application

**Option A: Windows One-Click Startup**

```bash
start_app.bat
```

This launcher is designed to start the backend and frontend development servers.

**Option B: Manual Startup**

Backend:

```bash
cd backend
python run.py
```

Frontend (open a separate terminal):

```bash
cd frontend
npm install
npm run dev
```

### 5. Access the Application

| Component | Local URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://127.0.0.1:5000/api |

## 🧠 Machine Learning Capabilities

The platform uses machine learning to support intelligent procurement operations:

- **Centre Recommendation:** Evaluates procurement centre suitability.
- **Slot Optimization:** Helps distribute farmer arrivals across available time slots.
- **ETA Prediction:** Estimates waiting times based on queue conditions.
- **Overload Detection:** Identifies potential congestion at procurement centres.
- **Demand Forecasting:** Estimates future crop arrivals.
- **Decision Intelligence:** Provides operational recommendations to procurement officers.

## 🔐 Security and Data Management

- Role-based access for farmers and procurement officers.
- Environment-based configuration for sensitive credentials.
- Backend API-based communication.
- Structured database management using SQLAlchemy ORM.
- Secure payment integration through the configured payment gateway.

## 🎯 Project Objectives

- Digitize agricultural procurement operations.
- Reduce unnecessary waiting times for farmers.
- Improve procurement centre resource utilization.
- Enable intelligent scheduling and allocation.
- Provide transparent procurement tracking.
- Support data-driven operational decisions through machine learning.

## 🌱 Future Enhancements

- Enhanced multilingual support.
- Integration with additional agricultural services.
- Improved predictive models using real-time procurement data.
- Expanded mobile accessibility.
- Advanced analytics and reporting.

## 👩‍💻 Project Information

**Project Name:** AgriProcure AI  
**Domain:** Artificial Intelligence, Machine Learning & Full-Stack Development  
**Application Area:** Agricultural Technology

---

⭐ If you find this project interesting, consider giving the repository a star!

**GitHub:** [Priyadharsini987](https://github.com/Priyadharsini987)
