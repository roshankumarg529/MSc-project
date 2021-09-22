# -*- coding: utf-8 -*-
"""
@author: Roshan kumar
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("lgb.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(sex,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI,Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---

    #sex	age	Race_Ethnicity	income	On_Insulin_Dia_Meds	Diag_DM/Pre_DM	Weight(kg)	Height(cm)	BMI	Upper_Leg_Length
# Upper_Arm_Length	Arm_Circum	Waist_Circum	Triceps_Skinfold
# Subscapular_Skinfold	Glycohemoglobin(%)	albumin	Blood_urea_nitrogen	Creatinine	Diabetes_level
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[sex,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI, Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine]])
    print(prediction)
    return prediction

#sex	age	Race/Ethnicity	income	On_Insulin/Dia_Meds	Diag_DM/Pre_DM	Weight(kg)	Height(cm)	BMI	Upper_Leg_Length
# Upper_Arm_Length	Arm_Circum	Waist_Circum	Triceps_Skinfold
# Subscapular_Skinfold	Glycohemoglobin(%)	albumin	Blood_urea_nitrogen	Creatinine	Diabetes_level


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sex = st.selectbox("Select your Gender",("Male","Female"))
    age = st.text_input("Age","Type Here")
    Race_Ethnicity = st.text_input("Race/Ethnicity","Type Here")

    income = st.text_input("Income","Type Here")
    On_Insulin_Dia_Meds = st.text_input("On_Insulin/Dia_Meds", "Type Here")
    Diag_DM_Pre_DM = st.text_input("Diag_DM/Pre_DM", "Type Here")
    Weight = st.text_input("Weight(cm)", "Type Here")
    Height= st.text_input("Height(cm)", "Type Here")
    BMI = st.text_input("BMI", "Type Here")
    Upper_Leg_Length = st.text_input("Upper_Leg_Length", "Type Here")
    Upper_Arm_Length = st.text_input("Upper_Arm_Length", "Type Here")
    Arm_Circum = st.text_input("Arm_Circum", "Type Here")
    Waist_Circum = st.text_input("Waist_Circum", "Type Here")
    Triceps_Skinfold = st.text_input("Triceps_Skinfold", "Type Here")
    Subscapular_Skinfold = st.text_input("Subscapular_Skinfold", "Type Here")
    albumin	= st.text_input("Albumin", "Type Here")
    Blood_urea_nitrogen = st.text_input("Blood_urea_nitrogen", "Type Here")
    Creatinine = st.text_input("Creatinine", "Type Here")

    if sex == "Male":
        sex == 1
    else:
        sex == 2

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(sex,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI,Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
