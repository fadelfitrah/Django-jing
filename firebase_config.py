import firebase_admin
from firebase_admin import credentials, firestore

# Inisialisasi Firebase
cred = credentials.Certificate("firebase/app.json") 
firebase_admin.initialize_app(cred)

# Koneksi ke Firestore
db = firestore.client()
