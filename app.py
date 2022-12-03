import streamlit as st
from deta import Deta

DETA_KEY = "a06jeh1v_GJmS8DEiFToMLujbKenNi4rKPKj4fMNr"

deta = Deta(DETA_KEY)

users = deta.Base("bmi")

# Input fields
age = st.number_input('Age:')
weight = st.number_input('Weight (in kg):')
height = st.number_input('Height (in cm):')
gender = st.radio('Gender:', ['Male', 'Female'])

# BMI calculation function
def calc_bmi(weight, height):
    result = (weight / (height / 100) ** 2)
    return result



if st.button('Submit'):

    if weight > 0 and height > 0:

        bmi = calc_bmi(weight, height)

        response = {
            'age': age,
            'weight': weight,
            'height': height,
            'bmi': bmi,
        }
        users.insert(response)
        st.write('Data saved to the database')
    else:
        st.write("Can you input relevant informations")


    

