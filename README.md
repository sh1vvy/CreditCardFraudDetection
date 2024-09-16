# Credit Card Fraud Detection API

This project hosts a fraud detection model as an API using Flask. The model is capable of predicting whether a transaction is fraudulent based on several input features provided in JSON format.

Training and Testing notebooks w/ Profile Reports for each stage available at link: https://drive.google.com/drive/folders/1zIDvSDvBLa2Tj3QNEDT0lMN3GsOwcmgH?usp=sharing
## Drive Structure
### Archive: old/deleted
### Final Notebooks: Notebooks used for training and testing the dataset
### Profiling Reports: Data checked/analysis at every few steps (during Explore stage)

#### Profiling Reports CAN ONLY be seen after downloading [due to the output being an HTML File]

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

The goal of this project is to provide a simple API that allows users to input transaction details and receive a prediction on whether the transaction is fraudulent or not. The model is built using machine learning techniques and is hosted using Flask. Training process, overview and documentation can be found in this repo.

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


# **Running the API**

To run the API locally, execute the following command:

   ```bash
   python app.py
   ```


#Usage

You can interact with the API using any HTTP client like Postman, Curl, or directly through a web browser.

# Example Input
To test the API, you can use the following JSON input:
```bash
{
    "trans_date_trans_time": "2019-01-02 01:06:37",
    "cc_num": 4613314721966,
    "merchant": "fraud_Rutherford-Mertz",
    "category": "grocery_pos",
    "amt": 281.06,
    "gender": "M",
    "street": "542 Steve Curve Suite 011",
    "city": "Collettsville",
    "zip": 28611,
    "lat": 35.9946,
    "long": -81.7266,
    "trans_num": "e8a81877ae9a0a7f883e15cb39dc4022",
    "unix_time": 1325466397,
    "merch_lat": 36.430124,
    "merch_long": -81.179483
}
```

# Example Output
The API will return a JSON response indicating whether the transaction is fraudulent:

```bash
{
    "prediction": "Not Fraud"
}
```

# Deployment
For deployment, you can consider using platforms like Heroku, AWS, or Render to host the API online.

Example Deployment Command
For a deployment with Gunicorn on a server:

```bash
gunicorn -w 4 app:app
```

# Technologies Used
- Flask: For building and serving the API.
- Scikit-learn: For machine learning model and preprocessing.
- TensorFlow/Keras: For deep learning (if applicable).
- Python: Core programming language.
- Gunicorn: WSGI server for running Flask.
- Joblib: For model serialization.

# Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Issues and bug reports are welcome.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
