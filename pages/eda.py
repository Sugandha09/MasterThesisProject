import streamlit as st
import sweetviz as sv
import pandas as pd
import streamlit.components.v1 as components

def app():
    st.header('Exploratory Data Analysis')
    #data=pd.read_csv('city_temp.csv')
    #data['Month']=data['Month'].astype('category')
    #data['Year']=data['Year'].astype('category')
    #data['Day']=data['Day'].astype('category')
    #data['City']=data['City'].astype('category')
    #advert_report = sv.analyze(data)
    #display the report
    #advert_report.show_html('edatemp.html')
    st.write('Click the following EDA link of City Tempersture dataset')
    st.write('https://mi-linux.wlv.ac.uk/~2048496/edatemp.html')
    
    #data1=pd.read_csv('westmidlands_crime.csv')
    #data1=data1.drop('Crime ID', axis=1)
    #data1=data1.drop('Context', axis=1)
    #advert_report1 = sv.analyze(data1)
    #display the report
    #advert_report1.show_html('edacrime.html')
    #components.iframe(src='edacrime.html', width=1100, height=1200, scrolling=True)
    st.write('Click the following EDA link of Westmidlands Crime dataset')
    st.write('https://mi-linux.wlv.ac.uk/~2048496/edacrime.html')
    
    #data2=pd.read_csv('melanoma-1.csv')
    #data2['year']=data2['year'].astype('category')
    #advert_report2 = sv.analyze(data2)
    #display the report
    #advert_report2.show_html('edamelanoma.html')
    #components.iframe(src='edamelanoma.html', width=1100, height=1200, scrolling=True)
    st.write('Click the following EDA link of Malignant Melanoma dataset')
    st.write('https://mi-linux.wlv.ac.uk/~2048496/edamelanoma.html')
