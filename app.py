
from PIL import Image
import streamlit as st
from utils import *
import pandas as pd
import numpy as np
from deta import Deta

DETA_KEY = "a06jeh1v_GJmS8DEiFToMLujbKenNi4rKPKj4fMNr"

deta = Deta(DETA_KEY)
users = deta.Base("bmi")

st.title("Z-score Hesaplama Uygulaması")

img = Image.open("hacettepe.jpg")
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
