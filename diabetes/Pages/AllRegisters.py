import streamlit as st
import pandas as pd
import Controllers.databasecontroller as databasecontroller

def RegisterList():
    st.title('All Registers')
    st.write('-------')
    raw_data = databasecontroller.get_all()
    column_names = ['id', 'id_patient', 'cpf', 'gender', 'age', 'urea', 'cr', 
    'hb1ac', 'chol', 'tg', 'hdl', 'ldl', 'vlsl', 'bmi', 'outcome']
    df = pd.DataFrame(raw_data, columns=column_names)
    df.set_index('id', inplace=True)
    st.write(df)

    id_selected = st.text_input('id to eliminate (left column)')
    
    if st.button('Delete'):
       databasecontroller.delete(id_selected)
       st.success('Successful Delete!')
    