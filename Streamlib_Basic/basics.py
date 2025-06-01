"""
Streamlit Basics

"""
import streamlit as st

st.title("Hello From AI Class! We are learning Streamlit ")
st.header("AI project")
st.subheader("Broadway")

st.text("We are students of AI class studying here at Broadways")

st.success("Congrats!!")
st.warning("Sorry!!!")
st.error("oyeee")

st.markdown("this is markdown header lever 1")

st.markdown("this is markdown header lever 2")


st.markdown("**this is markdown bold text**")

st.markdown("This is [link](www.strearmlit.io)")
st.markdown("This is list")
st.markdown("_ Item1:")
st.markdown("_ Item2:")
st.markdown("_ Item3:")

ex= ZeroDivisionError("You cannot Divide")
st.exception(ex)

is_checked= st.checkbox("I agree")
if is_checked:
    st.write("You agree")
else:
    st.write("Please agree it")

selected_gender = st.radio("Please Choose Your Gender:", ("Male","Female","Other"))
if selected_gender == "Male":
    st.write("You are male")
elif selected_gender == "Female":
    st.write("You are Female")
else:
    st.write("Join LGBTQ")

hobby = st.selectbox("Please choose your hobby: ",("Reading","Travelling","Codding"))
st.write(f"Your hobbies are{hobby}")

hobby = st.multiselect("Please choose your hobby: ",("Reading","Travelling","Codding"))
st.write(f"Your hobbies are{hobby}")

btn_submit = st.button("Submit")

if btn_submit:
    st.write("submitted")

blood_pressure= st.text_input("Enter your blodd pressure level: ")

st.text_area("Enter your introduction")

from PIL import Image

img = Image.open("D:\AI\download.jpg")
st.image(img,width=200)

st.slider("select leve",0.0,10.0,step =0.1)

st.write(range(10))
st.text(range(10))