from dotenv import load_dotenv
load_dotenv()
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Keep trained ML binaries outside the Python "models" package.
# Set ML_MODELS_DIR in .env when storing artifacts somewhere else.
MODELS_DIR = os.path.abspath(
    os.environ.get("ML_MODELS_DIR", os.path.join(BASE_DIR, "ml_artifacts"))
)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-change-this-secret')
    _raw_db_url = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'agri_procurement.db')}")
    if _raw_db_url:
        if _raw_db_url.startswith('postgres://'):
            _raw_db_url = _raw_db_url.replace('postgres://', 'postgresql://', 1)
        elif _raw_db_url.startswith('mysql://'):
            _raw_db_url = _raw_db_url.replace('mysql://', 'mysql+pymysql://', 1)
    SQLALCHEMY_DATABASE_URI = _raw_db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 3600,
    }

    # Trained ML artifacts are expected in ML_MODELS_DIR (default: ./ml_artifacts).
    CENTRE_RECOMMENDATION_MODEL = os.path.join(MODELS_DIR, 'centre_recommendation_model.joblib')
    DEMAND_FORECASTING_MODEL = os.path.join(MODELS_DIR, 'demand_forecasting_model.joblib')
    ETA_PREDICTION_MODEL = os.path.join(MODELS_DIR, 'eta_prediction_model.joblib')
    OFFICER_DECISION_INTELLIGENCE_MODEL = os.path.join(MODELS_DIR, 'officer_decision_intelligence_model.joblib')
    OVERLOAD_PREDICTION_MODEL = os.path.join(MODELS_DIR, 'overload_prediction_model.joblib')
    SMART_SLOT_ALLOCATION_MODEL = os.path.join(MODELS_DIR, 'smart_slot_allocation_model.joblib')

    RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID', '')
    RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET', '')
    RAZORPAY_CURRENCY = 'INR'

    WHATSAPP_API_KEY = os.environ.get('WHATSAPP_API_KEY', '')
    WHATSAPP_PHONE_NUMBER_ID = os.environ.get('WHATSAPP_PHONE_NUMBER_ID', '')
    WHATSAPP_SENDER_NUMBER = os.environ.get('WHATSAPP_SENDER_NUMBER', '')
