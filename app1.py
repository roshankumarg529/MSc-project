# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:20:31 2020

@author: Krish Naik
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: krish.naik
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
    sex = st.text_input("Variance","Type Here")
    age = st.text_input("skewness","Type Here")
    Race_Ethnicity = st.text_input("curtosis","Type Here")

    income = st.text_input("entropy","Type Here")
    On_Insulin_Dia_Meds = st.text_input("entropy", "Type Here")
    Diag_DM_Pre_DM = st.text_input("entropy", "Type Here")
    Weight = st.text_input("entropy", "Type Here")
    Height= st.text_input("entropy", "Type Here")
    BMI = st.text_input("entropy", "Type Here")
    Upper_Leg_Length = st.text_input("entropy", "Type Here")
    BMI = st.text_input("entropy", "Type Here")
    Arm_Circum = st.text_input("entropy", "Type Here")
    Waist_Circum = st.text_input("entropy", "Type Here")
    Triceps_Skinfold = st.text_input("entropy", "Type Here")
    Subscapular_Skinfold = st.text_input("entropy", "Type Here")
    albumin	= st.text_input("entropy", "Type Here")
    Blood_urea_nitrogen = st.text_input("entropy", "Type Here")
    Creatinine = st.text_input("entropy", "Type Here")



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
    
    
    