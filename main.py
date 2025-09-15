import streamlit as st

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

st.title("🧮 Factorial Calculator")
st.write("Enter a number below to calculate its factorial:")
num = st.number_input("Enter a number", min_value=0, step=1)
if st.button("Calculate Factorial"):
    result = factorial(num)
    st.success("The factorial of "+str( num) +"is"+ str(result))
