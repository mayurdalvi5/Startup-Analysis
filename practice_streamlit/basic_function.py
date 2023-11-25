import streamlit as st
import pandas as pd
import time

st.title("Startup Dashboard")   # title
st.header("I am learning Streamlit")   # header
st.subheader("And I am loving it")   # subheader
st.write("This is normal text")    # paragraph
st.markdown("""
### Prgramming Languages
- Python
- Java
- C++
""")
st.code("""
def add(a , b):
    return (a+b)
""")

st.latex("a^2 + b^2 + 1 =0")

df = pd.DataFrame({
    'Name': ['Mayur','Rahul','Danny'],
    'Age' : [24,26,75],
    'Class':['XII','VI','L']

})
st.dataframe(df)
st.metric("Revenue",'Rs 4L','5%')

st.json({
'Name': ['Mayur','Rahul','Danny'],
    'Age' : [24,26,75],
    'Class':['XII','VI','L']
})

st.image("123.png")
st.video('C:\\Users\\admin\\Videos\\SaMple.mkv')

st.sidebar.title("Sidebar Title")

col1, col2 = st.columns(2)

with col1:
    st.image('123.png')

with col2:
    st.image('123.png')


st.error("Login Failed")
st.success("Login Success")
st.info("Information ")
st.warning("Warning")

bar = st.progress(0)
for i in range(101):
    # time.sleep(0.1)
    bar.progress(i)

Email = st.text_input("Enter Email ")
PhoneNumber = st.number_input("Enter Phone Number ")
st.date_input("Enter Registation Data")