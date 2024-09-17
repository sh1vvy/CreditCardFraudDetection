


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model and preprocessors
model = joblib.load('trained_model.pkl')
category_enc = joblib.load('category_encoder.pkl')
street_enc = joblib.load('street_encoder.pkl')
gender_enc = joblib.load('gender_encoder.pkl')
city_enc = joblib.load('city_encoder.pkl')
merchant_enc = joblib.load('merchant_encoder.pkl')
trans_num_enc = joblib.load('trans_num_encoder.pkl')
trans_date_trans_time_enc = joblib.load('trans_date_trans_time_encoder.pkl')

class Transaction(BaseModel):
    trans_date_trans_time: int
    cc_num: int
    merchant: int
    category: int
    amt: float
    gender: int
    street: int
    city: int
    zip: int
    lat: float
    long: float
    trans_num: int
    unix_time: int
    merch_lat: float
    merch_long: float

def safe_transform(encoder, value):
    if value not in encoder.classes_:
        encoder.classes_ = np.append(encoder.classes_, value)
    return encoder.transform([value])[0]

@app.get("/")
def home():
    return {"message": "Welcome to the Fraud Detection API"}

@app.post("/predict/")
def predict(data: Transaction):
    # Encode each categorical variable using its respective encoder
    category_encoded = safe_transform(category_enc, data.category)
    street_encoded = safe_transform(street_enc, data.street)
    gender_encoded = safe_transform(gender_enc, data.gender)
    city_encoded = safe_transform(city_enc, data.city)
    merchant_encoded = safe_transform(merchant_enc, data.merchant)
    trans_num_encoded = safe_transform(trans_num_enc, data.trans_num)
    trans_date_trans_time_encoded = safe_transform(trans_date_trans_time_enc, data.trans_date_trans_time)

    # Combine all input features into a single array
    input_features = np.array([
        trans_date_trans_time_encoded,
        data.cc_num,
        merchant_encoded,
        category_encoded,
        data.amt,
        gender_encoded,
        street_encoded,
        city_encoded,
        data.zip,
        data.lat,
        data.long,
        trans_num_encoded,
        data.unix_time,
        data.merch_lat,
        data.merch_long
    ]).reshape(1, -1)  # Ensure the shape is (1, 15)

    # Make prediction
    prediction = model.predict(input_features)

    result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
    return {"prediction": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
