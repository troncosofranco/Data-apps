import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import Controllers.databasecontroller as databasecontroller

def data_visualization():
    st.title('Data visualization')
    raw_data = databasecontroller.get_all()
    column_names = ['id', 'id_patient', 'cpf', 'gender', 'age', 'urea', 'cr', 
    'hb1ac', 'chol', 'tg', 'hdl', 'ldl', 'vlsl', 'bmi', 'outcome']
    df = pd.DataFrame(raw_data, columns=column_names)
    df.set_index('id', inplace=True)
    st.write(df)
    
    
