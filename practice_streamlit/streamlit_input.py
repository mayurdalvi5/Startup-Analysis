import streamlit as st


Email = st.text_input('Enter Email')
Pass = st.text_input("Enter Password")
gender = st.selectbox('select Gender',['male','female', 'other'])

btn = st.button("Login")

if btn:
    if Email == 'mayur@gmail.com' and Pass == '1234':
        st.balloons()
        st.write(gender)
    else:
        st.error("Login Error")

