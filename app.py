from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and preprocessors
model = joblib.load(r'Pickle_Files_for_Encoders_and_Model\trained_model.pkl')
category_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\category_encoder.pkl')
street_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\street_encoder.pkl')
gender_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\gender_encoder.pkl')
city_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\city_encoder.pkl')
merchant_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\merchant_encoder.pkl')
trans_num_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\trans_num_encoder.pkl')
trans_date_trans_time_enc = joblib.load(r'Pickle_Files_for_Encoders_and_Model\trans_date_trans_time_encoder.pkl')

def safe_transform(encoder, value):
    if value not in encoder.classes_:
        encoder.classes_ = np.append(encoder.classes_, value)
    return encoder.transform([value])[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Encode each categorical variable using its respective encoder
    category_encoded = safe_transform(category_enc, data['category'])
    street_encoded = safe_transform(street_enc, data['street'])
    gender_encoded = safe_transform(gender_enc, data['gender'])
    city_encoded = safe_transform(city_enc, data['city'])
    merchant_encoded = safe_transform(merchant_enc, data['merchant'])
    trans_num_encoded = safe_transform(trans_num_enc, data['trans_num'])
    trans_date_trans_time_encoded = safe_transform(trans_date_trans_time_enc, data['trans_date_trans_time'])

    # Combine all input features into a single array
    input_features = np.array([
        trans_date_trans_time_encoded,
        data['cc_num'],
        merchant_encoded,
        category_encoded,
        data['amt'],
        gender_encoded,
        street_encoded,
        city_encoded,
        data['zip'],
        data['lat'],
        data['long'],
        trans_num_encoded,
        data['unix_time'],
        data['merch_lat'],
        data['merch_long']
    ]).reshape(1, -1)  # Ensure the shape is (1, 15)

    # Make prediction
    prediction = model.predict(input_features)

    result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)