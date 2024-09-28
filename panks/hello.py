import streamlit as st
import datetime

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")


st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="blue")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions=[
            "Laugh out loud.",
            "Get the popcorn.",
            "Never stop learning.",
        ],
    )

    if genre == ":rainbow[Comedy]":
        st.write("You selected comedy.")
    else:
        st.write("You didn't select comedy.")

    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

    def sqr(num):
        return num ** 2
    num = st.number_input("Enter a number")
    if (st.button('Calculate square')):
        result = sqr(num)
        st.text(result)