from os import write
#from numpy.core.fromnumeric import size
import streamlit as st
import Pages.AllRegisters as PageAllRegisters
import Pages.NewRegister as PageNewRegister
import Pages.Visualization as PageVisualization
import Pages.Prediction as PagePrediction

st.set_page_config(layout="wide")

#==========================================Sidebar=============================
st.sidebar.title('Menu')
page = st.sidebar.selectbox('Option', ['New Register', 'Delete Register', 'Visualize Data','Prediction'])

#======================================================================

if page == 'New Register':
    PageNewRegister.new_form() #call the function into the imported model
   

if page == 'Delete Register':
    PageAllRegisters.RegisterList() #call the function into the imported model

if page == 'Visualize Data':
    PageVisualization.data_visualization() #call the function into the imported model

if page == 'Prediction':
    PagePrediction.make_prediction() #call the function into the imported model


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)