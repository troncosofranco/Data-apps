import streamlit as st
import models.Register as Register
import Controllers.databasecontroller as databasecontroller

def new_form():
    st.title('New Register')
    st.write('-------')
    with st.form(key='include_case'):
        input_id_patient = st.text_input(label='Patient ID')
        input_cpf = st.text_input(label='CPF')
        input_gender = st.selectbox(label='Gender', options=['M','F'])
        input_age = st.text_input(label= 'Age (years)')
        
        input_urea = st.text_input(label='Urea')
        input_cr = st.text_input(label='Creatinine Ratio')
        input_hba1c = st.text_input(label='HbA1c')
        input_chol=st.text_input(label='Cholesterol')
        input_tg=st.text_input(label='Tryglyceride')
        input_hdl=st.text_input(label='HDL')
        input_ldl=st.text_input(label='LDL')
        input_vlsl=st.text_input(label='VLSL')
        input_bmi=st.text_input(label='Body Mass Index')
        input_outcome= st.selectbox(label='Diagnostic', options=['N','Y','P'])
        
        input_button_submit = st.form_submit_button('Send')

    #ID,No_Pation,Gender,AGE,Urea,Cr,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI,CLASS
    #raw data https://data.mendeley.com/datasets/wj9rwkp9c2/1

        if input_button_submit:
            Register.id_patient = input_id_patient
            Register.cpf = input_cpf
            Register.gender = input_gender
            Register.age = input_age
            Register.urea = input_urea
            Register.cr = input_cr
            Register.hb1ac = input_hba1c
            Register.chol = input_chol
            Register.tg =input_tg
            Register.hdl =input_hdl
            Register.ldl =input_ldl
            Register.vlsl =  input_vlsl
            Register.bmi = input_bmi
            Register.outcome =input_outcome

            databasecontroller.add(Register)

            st.success('Successful registration!')