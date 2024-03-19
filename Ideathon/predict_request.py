import requests
import json

# URL of the Flask app endpoint
url = "http://127.0.0.1:5000/predict_age"


# Sample input data (adjust this based on your model's input requirements)
input_data = {
    "haematocrit":44.6,
    "haemoglobin": 14,
    "erythrocyte": 6.86,
    "leucocyte": 6.3,
    "thrombocyte": 232,
    "mch":20.4,
    "mchc":31.4,
    "mcv":65
}

# Send a POST request to the /predict_age endpoint
response = requests.post(url, json=input_data)

# Check the response
if response.status_code == 200:
    # If the request was successful, print the predicted age
    print("Predicted Age:", response.json()['predicted_age'])
    
else:
    # If there was an error, print the error message
    print("Error:", response.text)
