import streamlit as st

st.title("La Gxoia Projekto Intake Form")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

if st.button("If you are happy and you know it, click here!"):
    st.write(f"Welcome to La Gxoia Projekto, {name}!")

age = st.slider("Select your age", 18, 100, 25)
st.write(f"Your selected age is: {age}")

# Add a hyperlink below
st.markdown('[Click here to go to the Intake Form](https://docs.google.com/forms/d/e/1FAIpQLSdLD2DDpemKF47H3PrFzo2PjzavKGuEfRFHK4YwHbH82MyMHw/viewform?usp=dialog)', unsafe_allow_html=True)
st.write(f"\n")
st.write(f"Once you complete the Intake Form, you will be added to our Waitlist.")
st.write(f"All the best!")

# end of code