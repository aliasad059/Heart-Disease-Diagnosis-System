# Heart-Disease-Diagnosis-System
A Fuzzy Expert System for Heart Disease Diagnosis
It predicts the heard disease for a specific user with 13 input fields in 3 steps:
- Fuzzification
- Inference
- Defuzzification

## Inputs
Input fields are:
- chest pain type
- blood pressure
- cholesterol
- resting blood sugar
- maximum heart rate 
- resting electrocardiography (ECG) 
- exercise 
- old peak (ST depression induced by exercise relative to rest)
- thallium scan
- sex
- age 

## Outputs
The output field refers to the presence of heart disease in the patient.\
It is integer valued from 0 (no presence) to 4 (distinguish presence (values 1, 2, 3, 4))

## Run
 Installing requirements:
 ```
 pip install -r requirements.txt
 ```
 
 Run system:
 ```
 python3 app.py
 ```
 
 Now you can enter user's input from [localhost:8448](localhost:8448) !
 
