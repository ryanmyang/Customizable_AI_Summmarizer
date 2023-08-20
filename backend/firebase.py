import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv


cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
