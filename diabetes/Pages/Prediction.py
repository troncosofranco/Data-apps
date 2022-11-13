import streamlit as st
import pickle
import numpy as np


loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

def make_prediction():
    st.title('Diabetes Prediction')
    st.write('-------')

    #Columns split
    col1, col2, col3 = st.columns(3)

    #normalized data input
    with col1:
        gender = st.selectbox(label='Gender', options=['M','F'])
        age = st.text_input('Age (20-79 years)')
        urea = st.text_input('Urea (0.5-38.9 mg/dL)')
        creatinine_ratio = st.text_input('Creatinine Ratio (6-80 μmol/L)')
    

    with col2:
        hb1ac = st.text_input('HBA1C (0.9-16 mmol/L)')
        cholestherol = st.text_input('Cholesterol (0.0-10.3 mmol/L)')
        triglycrerides = st.text_input('Triglycerides (0.3-13.8 mmol/L)')
        hdl = st.text_input('HDL (0.2-9.9 mmol/L)')
        
        
    with col3:
        ldl = st.text_input('LDL (0.3-9.9 mmol/L)')
        vldl = st.text_input('VLDL (0.1-35.0 mmol/L)')
        bmi = st.text_input('BMI (19-47.75)')
        

    if st.button('Predict'):
        if gender == 'F':
            gender = '0.0'
        else: 
            gender = '1.0'
        
        input_data = np.asarray([gender,	age, urea,	creatinine_ratio, 
        hb1ac, cholestherol, triglycrerides, hdl,  ldl,	vldl, bmi]).reshape(1,-1)
        max_vector = np.asarray([1.0, 79, 38.9, 80, 16, 10.3,13.8, 9.9,9.9, 35.0, 47.75]).reshape(1,-1)
        
        input_data = input_data.astype(np.float).reshape(1,-1)

        normalized_input = np.divide(input_data, max_vector)
        
        
        # loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))
        prediction = loaded_model.predict(input_data)
        prediction_proba = loaded_model.predict_proba(input_data)

        if (prediction[0] == 0):
            st.write(f'The person is not diabetic with a probability of {prediction_proba[0,0]*100}%')
            st.progress(prediction_proba[0,0])
            
        else:
            st.write(f'The person is diabetic with a probability of {prediction_proba[0,1]*100}%')
            st.progress(prediction_proba[0,1])
            


        
        
        


