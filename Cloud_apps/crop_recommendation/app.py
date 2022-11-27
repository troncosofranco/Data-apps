#Impor libraries
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# define model patch
MODEL_PATH = 'models/pickle_model.pkl'

def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


#main function
def main():
    model=''

    
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#04d12a;text-align:center;">Crop Recommendation </h1>
    </div>
    """

    #show html
    st.markdown(html_temp,unsafe_allow_html=True)

    # data input
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    N = st.text_input("Nitrogen Ratio:")
    P = st.text_input("Phosphorous Ratio:")
    K = st.text_input("Potassium Ratio:")
    Temp = st.text_input("Temperature [°C]:")
    Hum = st.text_input("Humidity [%]:")
    pH = st.text_input("pH:")
    rain = st.text_input("Rainfall [mm]:")
    
    if st.button("Recommendation"): 
    
        x_in =[np.float_(N.title()),
                    np.float_(P.title()),
                    np.float_(K.title()),
                    np.float_(Temp.title()),
                    np.float_(Hum.title()),
                    np.float_(pH.title()),
                    np.float_(rain.title())]
        prediction = model_prediction(x_in, model)
        st.success('The Crop recommmend is: {}'.format(prediction[0]).upper())
        

# Always running the main funciton
if __name__ == '__main__':
    main()