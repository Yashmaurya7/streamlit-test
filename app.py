import streamlit as st

st.title("Add Two Numbers")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

if st.button("Add"):
    result = num1 + num2
    st.success(f"The result is {result}")
