from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import joblib  # type: ignore
import os

app = Flask(__name__)
CORS(app) # Mengizinkan Prediksi.html (CORS) untuk mengakses API ini

# Memuat Model dan Scaler dari folder yang sama
try:
    # Sesuaikan path agar selalu membaca dari folder tempat app.py ini berada
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'svm_model_final.joblib')
    scaler_path = os.path.join(base_dir, 'scaler.joblib')
    
    svm_model_final = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("[SUCCESS] Model & Scaler berhasil dimuat!")
except Exception as e:
    print(f"[ERROR] Gagal memuat model atau scaler.")
    print(f"Pastikan file 'svm_model_final.joblib' dan 'scaler.joblib' sudah didownload dan ditaruh di folder yang sama dengan app.py")
    print(f"Detail error: {e}")

@app.route("/")
def home():
    return send_from_directory(base_dir, 'Prediksi.html')

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    try:
        content = request.json
        data = content.get('features', [])

        if not data or len(data) == 0:
            return jsonify({"error": "Data features kosong", "status": "failed"}), 400

        # Proses data menggunakan scaler dan model SVM
        input_data = np.array(data).reshape(1, -1)
        input_scaled = scaler.transform(input_data)
        prediction = svm_model_final.predict(input_scaled)
        
        # Coba ambil probabilitas jika model mendukung
        probability = 0.85 # Default fallback
        try:
            if hasattr(svm_model_final, "predict_proba"):
                probs = svm_model_final.predict_proba(input_scaled)
                probability = float(np.max(probs))
            elif hasattr(svm_model_final, "decision_function"):
                # Estimasi sederhana dari decision function
                df = svm_model_final.decision_function(input_scaled)
                probability = 1 / (1 + np.exp(-abs(df[0]))) # Sigmoid of distance
        except:
            pass

        result = "Churn" if prediction[0] == 1 else "No Churn"
        return jsonify({
            "prediction": result, 
            "probability": round(probability * 100, 2),
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("Menjalankan Server Web Lokal di: http://127.0.0.1:5000")
    print("Buka link di atas di browser Anda!")
    print("="*50 + "\n")
    app.run(port=5000, debug=True)
