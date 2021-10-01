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
def predict_note_authentication(s,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI,Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine):
   
   
    prediction=classifier.predict([[s,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI, Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine]])
    print(prediction)
    return prediction

#sex	age	Race/Ethnicity	income	On_Insulin/Dia_Meds	Diag_DM/Pre_DM	Weight(kg)	Height(cm)	BMI	Upper_Leg_Length
# Upper_Arm_Length	Arm_Circum	Waist_Circum	Triceps_Skinfold
# Subscapular_Skinfold	Glycohemoglobin(%)	albumin	Blood_urea_nitrogen	Creatinine	Diabetes_level


def main():
    st.title("Diabetic Risk Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetic Risk Prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sex = st.selectbox("Select your Gender",("Male","Female"))
    age = st.text_input("Age")
    Race_Ethnicity = st.selectbox("Select your Race/Ethnicity",("Mexican American","Non-Hispanic White","Non-Hispanic Black","Other Hispanic","Other Race Including Multi-Racial"))

    income = st.text_input("Income")
    On_Insulin_Dia_Meds = st.text_input("On_Insulin/Dia_Meds")
    Diag_DM_Pre_DM = st.text_input("Diag_DM/Pre_DM")
    Weight = st.text_input("Weight(cm)")
    Height= st.text_input("Height(cm)")
    BMI = st.text_input("BMI")
    Upper_Leg_Length = st.text_input("Upper_Leg_Length")
    Upper_Arm_Length = st.text_input("Upper_Arm_Length")
    Arm_Circum = st.text_input("Arm_Circum")
    Waist_Circum = st.text_input("Waist_Circum")
    Triceps_Skinfold = st.text_input("Triceps_Skinfold")
    Subscapular_Skinfold = st.text_input("Subscapular_Skinfold")
    albumin	= st.text_input("Albumin", "Type Here")
    Blood_urea_nitrogen = st.text_input("Blood_urea_nitrogen")
    Creatinine = st.text_input("Creatinine")
    
    s = 0
    if sex == "Male":
        s == 1
    else:
        s == 2

    Race = 0
    if (Race_Ethnicity == "Non-Hispanic White"):
        Race == 1
    elif (Race_Ethnicity == "Non-Hispanic Black"):
        Race == 2
    elif (Race_Ethnicity == "Mexican American"):
        Race == 3
    elif (Race_Ethnicity == "Other Hispanic"):
        Race == 4
    elif (Race_Ethnicity == "Other Race Including Multi-Racial"):
        Race == 5
        
        
        
        
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(s,age,Race_Ethnicity,income,On_Insulin_Dia_Meds, Diag_DM_Pre_DM,
                                Weight,	Height,	BMI,Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine)
    res = ""
    if (result == 0):
        res = "You are Risk Free"
    if (result == 1):
        res = "You have the Risk of Pre-Diabetic"
    if (result == 2):
        res = "You are on the Hight-Risk of Diabetic Please consult the doctor"
     
    st.success(res)
    if st.button("About"):
        st.text("MSc project")
        #st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
