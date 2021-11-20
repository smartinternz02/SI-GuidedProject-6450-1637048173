# Import libraries
import numpy as np
import requests
from flask import Flask, request, jsonify, render_template


import json

API_KEY = "i5aJIQr0hEeEd2WG3HGZDoQkZX8GJnNDgfJZHnK5Ai7L"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index20.html')


@app.route('/y_predict',methods=['POST'])
def y_predict():
    age =request.form.get["age"]
    sex = request.form.get["sex"]
    cp = request.form.get["cp"]
    trestbps = request.form.get["trestbps"]
    chol = request.form.get["chol"]
    fbs = request.form.get["fbs"]
    restecg = request.form.get["restecg"]
    thalach = request.form.get["thalach"]
    exang = request.form.get["exang"]
    oldpeak = request.form.get["oldpeak"]
    slope = request.form.get["slope"]
    ca = request.form.get["ca"]
    thal = request.form.get["thal"]
    
    
    

     
    
    print(age)
    print(sex)
    print(cp)
    print(trestbps)
    print(chol)
    print(fbs)
    print(restecg)
    print(thalach)
    print(exang)
    print(oldpeak)
    print(slope)
    print(ca)
    print(thal)
    
    
    data_val = [[int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]]

    payload_scoring = {"input_data": [{"fields": [["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]],
                                       "values": data_val
                                       }]}

    response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/86bf09fc-2a00-40d5-8356-8d95d5917897/predictions?version=2021-10-25', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    predictions = (predictions)
    pred = predictions['predictions'][0]['values'][0][0]
    if(pred == 0):
        output = "The Person does not have a Heart Disease"
        print("The Person does not have a Heart Diseas")
    else:
        output = "The Person has Heart Disease"
        print("The Person has Heart Disease")
   
    

    return render_template('index20.html', prediction_text=output)

# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)
