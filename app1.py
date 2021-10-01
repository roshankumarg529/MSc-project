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
def predict_note_authentication(s,age,Race,incm,onIn, Predb,
                                Weight,	Height,	BMI,Upper_Leg_Length,Upper_Arm_Length,
                                Arm_Circum,	Waist_Circum,	Triceps_Skinfold,Subscapular_Skinfold, albumin,
                                Blood_urea_nitrogen, Creatinine):
   
   
    prediction=classifier.predict([[s,age,Race,incm,onIn, Predb,
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
    sex = st.selectbox("Select your Gender",("--select--","Male","Female"))
    age = st.text_input("Age")
    Race_Ethnicity = st.selectbox("Select your Race/Ethnicity",("--select--","Mexican American","Non-Hispanic White","Non-Hispanic Black","Other Hispanic","Other Race Including Multi-Racial"))

    income = st.selectbox("Income per month", ("--select--","<5000", "Greater than 5000 & Less than 10000" ,"Greater than or equal to 10000 & Less than 15000" ,"Greater than or equal to 15000 & Less than 20000" ,"Greater than or equal to 20000 & Less than 25000" ,
                                              "Greater than or equal to 25000 & Less than 35000" ,"Greater than or equal to 35000 & Less than 45000" ,"Greater than or equal to 45000 & Less than 55000" ,
                                              "Greater than 55000 & Less than 65000" ,
                                              "Greater than or equal to 65000 & Less than 75000" ,"Greater than or equal to 75000 & Less than 100000" ,">= 100000"))
    On_Insulin_Dia_Meds = st.selectbox("On_Insulin/Dia_Meds", ("--select--","Yes", "No"))
    Diag_DM_Pre_DM = st.selectbox("Diag_DM_Pre_DM", ("--select--","Yes", "No"))
    Weight = st.text_input("Weight(kg)")
    Height= st.text_input("Height(cm)")
    BMI = st.text_input("BMI (kg/m^2")
    Upper_Leg_Length = st.text_input("Upper_Leg_Length (cm)")
    Upper_Arm_Length = st.text_input("Upper_Arm_Length (cm)")
    Arm_Circum = st.text_input("Arm_Circum (cm)")
    Waist_Circum = st.text_input("Waist_Circum (cm)")
    Triceps_Skinfold = st.text_input("Triceps_Skinfold (mm)")
    Subscapular_Skinfold = st.text_input("Subscapular_Skinfold (mm)")
    albumin	= st.text_input("Albumin (g/dL)")
    Blood_urea_nitrogen = st.text_input("Blood_urea_nitrogen (mg/dL)")
    Creatinine = st.text_input("Creatinine (mg/dL)")
    
    s = 0
    if sex == "Male":
        s = 1
    else:
        s = 2

    Race = 0
    if (Race_Ethnicity == "Non-Hispanic White"):
        Race = 1
    elif (Race_Ethnicity == "Non-Hispanic Black"):
        Race = 2
    elif (Race_Ethnicity == "Mexican American"):
        Race = 3
    elif (Race_Ethnicity == "Other Hispanic"):
        Race = 4
    elif (Race_Ethnicity == "Other Race Including Multi-Racial"):
        Race = 5
        
        
    onIn = 0
    
    if (On_Insulin_Dia_Meds == "Yes"):
        onIn = 1
    else:
        onIn = 0
 

    Predb = 0
    
    if (Diag_DM_Pre_DM == "Yes"):
        Predb = 1
    else:
        Predb = 0
        
    incm = 0
   
    if (income ==  "<5000"):
        incm = 1
    elif (income == "Greater than 5000 & Less than 10000"):
        incm = 2
    elif (income == "Greater than or equal to 10000 & Less than 15000"):
        incm = 3                          
    elif (income == "Greater than or equal to 15000 & Less than 20000"):
        incm = 4                          
    elif (income == "Greater than or equal to 20000 & Less than 25000"):
        incm = 5                          
    elif (income == "Greater than or equal to 25000 & Less than 35000"):
        incm = 6                                              
    elif (income == "Greater than or equal to 35000 & Less than 45000"):
        incm = 7                                             
    elif (income == "Greater than or equal to 45000 & Less than 55000" ):
        incm = 8                                           
    elif (income == "Greater than or equal to 55000 & Less than 65000"):
        incm = 9                                             
    elif (income == "Greater than or equal to 65000 & Less than 75000"):
        incm = 10                                             
    elif (income == "Greater than or equal to 75000 & Less than 100000" ):
        incm = 11                         
    elif (income == ">= 100000"):
        incm = 12                          
                          
                          
                          
                          
                          
                          
                          
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(s,age,Race,incm,onIn, Predb,
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
    
    
    
