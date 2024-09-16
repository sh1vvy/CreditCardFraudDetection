# Fraud Detection API

This project hosts a fraud detection model as an API using Flask. The model is capable of predicting whether a transaction is fraudulent based on several input features provided in JSON format.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Running the API](#running-the-api)
- [Usage](#usage)
- [Example Input](#example-input)
- [Example Output](#example-output)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to provide a simple API that allows users to input transaction details and receive a prediction on whether the transaction is fraudulent or not. The model is built using machine learning techniques and is hosted using Flask.

## Setup Instructions

To get started with this project, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sh1vvy/creditcardfrauddetection.git
   
2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Loading pre-trained model**
5. **Running the API**
   ```bash
   python app.py

#Usage

You can interact with the API using any HTTP client like Postman, Curl, or directly through a web browser.

Example Input
To test the API, you can use the following JSON input:
{
    "trans_date_trans_time": 1622505600,
    "cc_num": 1234567890123456,
    "merchant": "merchant_name",
    "category": "category_name",
    "amt": 100.50,
    "gender": "M",
    "street": "1234 Main St",
    "city": "New York",
    "zip": 10001,
    "lat": 40.7128,
    "long": -74.0060,
    "trans_num": "12345abcde",
    "unix_time": 1622505600,
    "merch_lat": 40.7328,
    "merch_long": -74.0160
}

Example Output
The API will return a JSON response indicating whether the transaction is fraudulent:

{
    "prediction": "Not Fraud"
}


#Deployment
For deployment, you can consider using platforms like Heroku, AWS, or Render to host the API online.

Example Deployment Command
For a deployment with Gunicorn on a server:

 
