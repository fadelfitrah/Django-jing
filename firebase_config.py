import firebase_admin
from firebase_admin import credentials, firestore

# Inisialisasi Firebase
cred = credentials.Certificate("firebase/to-do-list-63f8e-firebase-adminsdk-fbsvc-c2a0a4dfa3.json")  # Ganti dengan path yang benar
firebase_admin.initialize_app(cred)

# Koneksi ke Firestore
db = firestore.client()
