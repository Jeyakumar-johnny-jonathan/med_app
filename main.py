from flask import Flask, jsonify, request
import pandas as pd
import os
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

#chadsvasc
app = Flask(__name__)

@app.route("/get_chadsvasc", methods = ['POST'])

def get_chadsvasc():

    if request.method == "POST":
        req_json = json.loads(request.data)
        congestive_heart_failure = req_json["congestive heart failure"]
        hypertension = req_json["hypertension"]
        age = req_json["age"]
        diabetes_mellitus = req_json["diabetes_mellitus"]
        stroke_or_TIA_or_thromboembolism = req_json["stroke_or_TIA_or_thromboembolism"]
        vascular_disease = req_json["vascular_disease"]
        sex = req_json["sex"]

        #congestive_heart_failure
        if congestive_heart_failure == "yes":
            congestive_heart_failure_value = 1
            
        else:
            congestive_heart_failure_value = 0

        #hypertension
        if hypertension > 140:
            hypertension_value = 1

        else:
            hypertension_value = 0

        #age
        if age >= 75:
            age_value = 2

        elif age >= 65:
            age_value = 1

        else:
            age_value = 0

        #diabetes_mellitus
        if diabetes_mellitus == "yes":
            diabetes_mellitus_value = 1
        else:
            diabetes_mellitus_value = 0

        #stroke_or_TIA_or_thromboembolism
        if stroke_or_TIA_or_thromboembolism == "yes" :
            stroke_or_TIA_or_thromboembolism_value = 2

        else:
            stroke_or_TIA_or_thromboembolism_value= 0

        #sex
        if sex == "female":
            sex_value = 1

        else:
            sex_value = 0

        #calculating value
        chadsvasc_value = congestive_heart_failure_value + hypertension_value + age_value + diabetes_mellitus_value +  stroke_or_TIA_or_thromboembolism_value + sex_value

        if (chadsvasc_value == 0) and (sex == "male") :
            chadsvasc_result = "Low"

        elif (chadsvasc_value == 1) and (sex == "female") :
            chadsvasc_result = "Low"

        elif (chadsvasc_value == 1) and (sex == "male"):
            chadsvasc_result = "Moderate"

        else:
            chadsvasc_result = "High"
                   

    return jsonify({'CHADSVASC_result' : chadsvasc_result})    

#has_bled
@app.route("/get_has_bled_score", methods = ['POST'])

def get_has_bled_score():

    if request.method == "POST":
        req_json = json.loads(request.data)
        hypertension = req_json["hypertension_mmHg"]
        abnormal_renal = req_json["abnormal_renal_mg/dL"]
        liver_function = req_json["liver_function"]
        stroke = req_json["stroke"]
        bleeding = req_json["bleeding"]
        labile_inr = req_json["labile_inr_percentage"]
        elderly = req_json["elderly"]
        drugs_or_alcohol = req_json["drugs_or_alcohol"]

    #hypertension
    if hypertension > 160:
        hypertension_value = 1

    else:
        hypertension_value = 0

    #abnormal_renal
    if abnormal_renal > 2.26:
        abnormal_renal_value = 1
        
    else:
        abnormal_renal_value = 0

    #liver_function
    if liver_function > 200:
        liver_function_value = 1

    else:
        liver_function_value = 0

    #stroke
    if stroke == "yes":
        stroke_value = 1

    else:
        stroke_value = 0

    #Bleeding
    if bleeding == "yes":
        bleeding_value = 1

    else:
        bleeding_value = 0

    #labile_inr
    if labile_inr < 60:
        labile_inr_value = 1

    else:
        labile_inr_value = 0

    #elderly
    if elderly > 65:
        elderly_value = 1

    else:
        elderly_value = 0

    #Drugs or alcohol

    if drugs_or_alcohol == "yes":
        drugs_or_alcohol_value = 1

    else:
        drugs_or_alcohol_value = 0


    has_bled = hypertension_value + abnormal_renal + liver_function + stroke_value + bleeding_value + labile_inr_value + elderly_value + drugs_or_alcohol_value

    #HAS-BLED value check

    if has_bled == 0:
        has_bled_value = "Low"

    elif 1 <= has_bled <= 3:
        has_bled_value = "Moderate"

    else:
        has_bled_value = "High"
        
        
        
    
    return jsonify({'HAS_BLED_score' : has_bled_value})


# Cholestrol and diabetes mellitus       
@app.route("/get_data", methods = ['POST'])

def get_data():

    if request.method == "POST":
        req_json = json.loads(request.data)
        diabetes = req_json["diabetes"]
        cholestrol_value = req_json["cholestrol_value"]
        age = req_json["age"]
        smoking_value = req_json["smoking_value"]
        gender_value = req_json["gender_value"]
        sbp_value = req_json["sbp_value"]



    #age catorization
        if age < 40:
            age_category = "40-50"

        elif 40 <= age <= 50:
            age_category = "40-50"

        elif 50 <= age <= 60:
            age_category = "50-60"

        elif 60 <= age <= 70:
            age_category = "60-70"

        elif 70 <= age <= 80:
            age_category = "70-80"

        else:
            age_category = "70-80"

            
        #Cholestrol value
        if cholestrol_value <= 4:
            cholestrol_value = 4

        elif 4 < cholestrol_value <= 5:
            cholestrol_value = 5

        elif 5 < cholestrol_value <= 6:
            cholestrol_value = 6

        elif 6 < cholestrol_value <=7:
            cholestrol_value = 7

        else:
            cholestrol_value = 8

        #SBP Value check
        if sbp_value < 120:
            sbp_value = 120

        elif 120 < sbp_value <=140:
            sbp_value = 140

        elif 140 < sbp_value <= 160:
            sbp_value = 160

        else:
            sbp_value = 180

         #Gender   
        if gender_value == "male":
            gender_value = "m"

        else:
            gender_value = "f"

        #smoking
        if smoking_value == "yes":
            smoking_value = "y"

        else:
            smoking_value = "n"

        





    #patient with diabetics and with cholestrol
    if diabetes == "yes":
        if cholestrol_value != "no":
            with_diabetes_mellitus = pd.read_csv(dir_path + "/with_cholesterol_Diabetes_Mellitus.csv")
            df1 = with_diabetes_mellitus
            risk = df1.loc[(df1["Age"] == age_category) & (df1["Smoking"] == smoking_value) & (df1["Gender"] == gender_value) & (df1["SBP"]==sbp_value) & (df1["Cholestrol"] == cholestrol_value)]
            
            
    #patient with diabetics and without cholestrol
        else:
            without_diabetes_mellitus = pd.read_csv(dir_path + "/without_cholestrol_Diabetes_Mellitus.csv")
            df1 = without_diabetes_mellitus
            risk = df1.loc[(df1["Age"] == age_category) & (df1["Smoking"] == smoking_value) & (df1["Gender"] == gender_value) & (df1["SBP"]==sbp_value)]
            

    #patient without diabetics and with cholestrol
    else:
        if cholestrol_value != "no":
            with_diabetes_mellitus = pd.read_csv(dir_path + "/with_cholesterol_without_Diabetes_Mellitus.csv")
            df1 = with_diabetes_mellitus
            risk = df1.loc[(df1["Age"] == age_category) & (df1["Smoking"] == smoking_value) & (df1["Gender"] == gender_value) & (df1["SBP"]==sbp_value) & (df1["Cholestrol"] == cholestrol_value)]
            

    #patient without diabetics and without cholestrol
        else:
            without_diabetes_mellitus = pd.read_csv(dir_path + "/without_cholesterol_without_Diabetes_Mellitus.csv")
            df1 = without_diabetes_mellitus
            risk = df1.loc[(df1["Age"] == age_category) & (df1["Smoking"] == smoking_value) & (df1["Gender"] == gender_value) & (df1["SBP"]==sbp_value)]

    # Output risk value

    if risk["Risk"].values[0]== 0:
        risk_value = "Low"

    elif risk["Risk"].values[0]== 1:
        risk_value = "Moderate"

    elif risk["Risk"].values[0]== 2:
        risk_value = "Moderately_high"

    elif risk["Risk"].values[0]== 3:
        risk_value = "High"

    else :
        risk_value = "Severe"
        
            

    return jsonify({'risk_value' : risk_value})


    




if __name__ == "__main__":
    app.run()
  
