import requests

# The URL for the local FastAPI server
url = "http://127.0.0.1:8000/predict"

# Example JSON input based on your model's expected features
data = {
    "trans_date_trans_time": 0,
    "cc_num": 2703186189652095,
    "merchant": 514,
    "category": 8,
    "amt": 4.97,
    "gender": 0,
    "street": 568,
    "city": 526,
    "zip": 28654,
    "lat": 36.0788,
    "long": -81.1781,
    "trans_num": 56438,
    "unix_time": 1325376018,
    "merch_lat": 36.011293,
    "merch_long": -82.048315
}


# Sending a POST request with JSON input
response = requests.post(url, json=data)

# Printing the response
print(response.json())
