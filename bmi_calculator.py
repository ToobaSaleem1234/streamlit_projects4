# Create a Python Streamlit BMI Calculator in just 6 minutes:
import streamlit as st

# display app:
st.set_page_config(page_title="BMI Calculator", page_icon="🤫", layout='centered')

# title of the app:
st.header("Body Mass Index (BMI) Calculator 🔄")
st.status("Calculate your BMI and find out your weight category based on your weight and height 👀 ")

# change height into meters:
length = st.number_input("Enter your height to change in meters (e.g 5.2):" , min_value=1.00 , format='%.2f')
if st.checkbox("📏 Calculate height"):
    change_height = length / 3.281
    st.success(f'Your height is {change_height: .2f} meters')

# input for height:
height = st.number_input("Enter your height in meters (e.g 1.75):",min_value= 1.0, format="%.2f")

# input for weight:
weight = st.number_input("Enter your weight in kilograms(e.g 50):", min_value= 1.0 , format= "%.2f")

# BMI Calculator:
if st.checkbox("📊 Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / height ** 2   # BMI formula:
        st.success(f"Your BMI is :{bmi : .2f}")

        # BMI Category:
        if bmi < 18.5 :
            st.info("You are underweight 😟")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight 😃")
            st.balloons()
        elif 24.9 <= bmi < 29.9:
            st.warning("You are overweight 😟")
        else:
            st.error("You are obese 😟")
    else:
        st.error("Enter a valid height and weight to calculate BMI")