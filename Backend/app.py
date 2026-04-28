from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# ===============================
# LOAD MODEL
# ===============================
MODEL_PATH = 'model.pkl'

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model tidak ditemukan! Jalankan train_model.py dulu.")

model = joblib.load(MODEL_PATH)


# ===============================
# ROUTE HOME
# ===============================
@app.route('/')
def home():
    return jsonify({
        "message": "API Prediksi Penyakit Aktif",
        "endpoint": "/predict (POST)"
    })


# ===============================
# VALIDASI INPUT
# ===============================
def validate_input(data):
    required_fields = ['umur', 'suhu', 'batuk']

    for field in required_fields:
        if field not in data:
            return False, f"Field '{field}' wajib diisi"

    try:
        umur = int(data['umur'])
        suhu = float(data['suhu'])
        batuk = int(data['batuk'])
    except:
        return False, "Format input tidak valid (umur=int, suhu=float, batuk=int)"

    return True, (umur, suhu, batuk)


# ===============================
# ENDPOINT PREDIKSI
# ===============================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request harus dalam format JSON"}), 400

        # validasi
        valid, result = validate_input(data)
        if not valid:
            return jsonify({"error": result}), 400

        umur, suhu, batuk = result

        # format input untuk model
        input_data = [[umur, suhu, batuk]]

        # prediksi
        prediction = model.predict(input_data)[0]

        return jsonify({
            "input": {
                "umur": umur,
                "suhu": suhu,
                "batuk": batuk
            },
            "prediksi": prediction
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ===============================
# RUN SERVER
# ===============================
if __name__ == '__main__':
    app.run(debug=True)