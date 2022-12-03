
from PIL import Image
import streamlit as st
from utils import *
import pandas as pd
import numpy as np
from deta import Deta
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html


with st.sidebar:
    choose = option_menu("Hacettepe Büyüme & Gelişim", ["Z skoru", "Gelişim Basamakları"],
                         icons=['bi bi-calculator-fill', 'bi bi-arrows-fullscreen'],
                         # icons = https://icons.getbootstrap.com/
                         menu_icon="app-indicator", 
                         default_index=0,
                         styles={
                                "container": {"padding": "5!important", },#"background-color": "#fafafa"
                                "icon": {"font-size": "25px"}, #"color": "orange"
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px" },#"--hover-color": "#eee"
                               #"nav-link-selected": {"background-color": "#02ab21"},
                                }
                        )

# logo = Image.open('https://github.com/turkalpmd/turkalpmd.github.io/blob/master/assets/img/apple-touch.png')
# profile = Image.open('https://github.com/turkalpmd/turkalpmd.github.io/blob/master/assets/img/turkalpmd.jpg')



if choose == "Z skoru":
    # col1, col2 = st.columns( [0.8, 0.2])
    # with col1:               # To display the header text using css style   with col2:    
    DETA_KEY = "a06jeh1v_GJmS8DEiFToMLujbKenNi4rKPKj4fMNr"

    deta = Deta(DETA_KEY)
    users = deta.Base("bmi")



    st.title("Z-score Hesaplama Uygulaması")

    img = Image.open("./images/hacettepe.jpg")
    st.image(img)

    # Introduction

    st.subheader("Büyüme Takibi")


    st.text("""
    Bu uygulamada Z score'lar 2 yaş ve altında WHO üstünde ise \n
    CDC referans aralıkları kullanılarak hesaplanır.\n
    Hizmet kalitesinde artış amaçlı olarak girdiğiniz veriler kayıt altına alınacaktır.
        """)


    weight = st.number_input("KG cinsinden ağırlık;", step = 1)
    height = st.number_input("Santimetre cinsinden boyu;", step = 1)
    age = st.number_input("Ay olarak yaşı;",step=1)
    gender =st.radio("Cinsiyeti seçiniz", options=["Erkek","Kız"])
        #text_input("Erkek için E Kız için K yazınız;")

    if gender == "Erkek":
        gender = "M"
    if gender == "Kız":
        gender = "F"

    if st.button("Z skorunu Analiz Et"):



        wfa, lhfa = calc(weight,height,age,gender)#result = process_csv(dataframe)
        wfa = float(str(wfa))
        lhfa = float(str(lhfa))
        
        st.success(f"Yaşa göre ağırlık; {wfa}") 
        st.success(f"Yaşa göre boy; {lhfa}") #st.success(f"Sonuç: {result}")
        
        response = {
                        'age': age,
                        'weight': weight,
                        'height': height,
                        'gender': gender,
                        'wfa':wfa,
                        'lhfa':lhfa
                    }
        users.insert(response)
        st.text("Bilgiler Database'e aktarıldı")

if choose == "Gelişim Basamakları":

    st.write("Hazırlanıyor",size=32)
    img = Image.open("./images/developmental_steps.jpg")
    st.image(img)





#https://medium.com/codex/create-a-multi-page-app-with-the-new-streamlit-option-menu-component-3e3edaf7e7ad
# pipreqs --savepath=requirements.txt && pip-compile 