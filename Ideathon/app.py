from flask import request, jsonify

from flask import Flask
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from flask_cors import CORS



# Create a Flask app
app = Flask(__name__)
CORS(app)

# Load your dataset (Assuming CSV format)
dataset_path = "C:\\Users\\kaggle2.csv"
data = pd.read_csv(dataset_path)

# Assuming 'age' is the target variable and other columns are features
X = data[['haematocrit', 'haemoglobin', 'erythrocyte', 'leucocyte', 'thrombocyte', 'mch', 'mchc', 'mcv']]
y = data['age']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create a route for prediction

@app.route('/predict_age', methods=['POST'])
def predict_age():
    # Your existing code for handling the prediction

    # Get data from the frontend
    input_data = request.get_json()

    # Prepare the input data as a DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Make a prediction using the trained model
    predicted_age = model.predict(input_df)

    # Return the predicted age as JSON
    
    return jsonify({'predicted_age': predicted_age[0]})



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)