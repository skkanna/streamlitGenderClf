# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: KamalaKannan Sampath
"""
#!pip3 install -U Flask
#from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
#import flasgger
#from flasgger import Swagger

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def gender_pred(is_installed, is_active, longitude, latitude,
                                      device_model, phone_brand, category, age):
    
    
    """Let's look at the Price Listing
    This is using docstrings for specifications.
    ---
    parameters:  
        
      - name: is_installed
        in: query
        type: number
        required: true
      - name: is_active
        in: query
        type: number
        required: true
      - name: longitude
        in: query
        type: number
        required: true
      - name: latitude
        in: query
        type: number
        required: true
      - name: device_model
        in: query
        type: number
        required: true
      - name: phone_brand
        in: query
        type: number
        required: true
      - name: category
        in: query
        type: number
        required: true
      - name: age
        in: query
        type: number
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    prediction=classifier.predict([[is_installed, is_active, longitude, latitude,
                                      device_model, phone_brand, category, age]])
    print(prediction)
    return prediction

#@app.route('/predict_file',methods=["Post"])
def main():
    st.title("Gender Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Gender Predictor ML App </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)    
#    v = st.number_input('Test', value=1.)
    
    is_installed = st.number_input("is_installed", value=1.)
    is_active = st.number_input("is_active", value=1.)
    longitude = st.number_input("longitude", value=1.)
    latitude = st.number_input("latitude", value=1.)
    device_model = st.number_input("device_model", value=1.)
    phone_brand = st.number_input("phone_brand", value=1.)
    category = st.number_input("category", value=1.)
    age = st.number_input("age", value=1.)
    
    
    
    result=""
    if st.button("Predict"):
                
        result=gender_pred(is_installed, is_active, longitude, latitude,
                                      device_model, phone_brand, category, age)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")  
    
if __name__=='__main__':
    main()