# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:50:14 2023

@author: starj
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("C:/Users/starj/OneDrive/Desktop/Multiple/savedmodel/dia_trained_model.sav",'rb'))
heart_model = pickle.load(open("C:/Users/starj/OneDrive/Desktop/Multiple/savedmodel/hrt_trained_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction','Heart Disease Prediction'],
                          icons=['heart','activity'],
                          default_index=0)
    
if(selected =='Diabetes Prediction'):
    st.title("Diabetes Prediction using ML")
    
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies") 
    
    with col2:
        Glucose = st.text_input("Glocose value")
    
    with col3:
        BloodPressure = st.text_input("BP value")
    
    with col1:
        SkinThickness = st.text_input("Skin thickness value")
    
    with col2:
        Insulin = st.text_input("Insulin value")
    
    with col3:
        BMI = st.text_input("Bmi Value")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    
    with col2:
        Age= st.text_input("Age")
    
    diagnosis = ''
    
    if(st.button('Test Result')):
        predcn = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(predcn[0]==0):
            diagnosis="Yor are non Diabetic.👍👍"
        else:
            diagnosis='You are Diabetic. Please contact a doctor immidiately.🩺'
        
    st.success(diagnosis)
    
if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction using ML")
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age") 
    
    with col2:
        sex = st.number_input("Sex")
    
    with col3:
        cp = st.number_input("Chest Pain Type")
    
    with col1:
        trestbps = st.number_input("Resting BP value")
    
    with col2:
        chol = st.number_input("Cholesterol value")
    
    with col3:
        fbs = st.number_input("Fasting Blood Suger Value")
    
    with col1:
        restecg = st.number_input(" Restecg Value")
    
    with col2:
        thalach= st.number_input("Thalach")
        
    with col3:
        exang = st.number_input("Excercise Induced Angina value")
     
    with col1:
        oldpeak = st.number_input("Skin thickness value")
     
    with col2:
        slope = st.number_input("Oldpeak")
     
    with col3:
        ca = st.number_input("CA Value")
     
    with col1:
        thal = st.number_input("Thal Value")
        
    heart_diag = ''
    
    if st.button("Prediction Result"):
        pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(pred[0]==0):
            heart_diag="Non Heart Disease"
        else:
            heart_diag='Contact Doctor'
    st.success(heart_diag)