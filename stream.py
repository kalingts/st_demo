import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
  result = num1 + num2
elif operation == "Subtract":
  result = num1 - num2
elif operation == "Multiply":
  result = num1 * num2
elif operation == "Divide":
  if num2 == 0:
    result = "Division by zero not allowed"
  else:
    result = num1 / num2
else:
  result = "Invalid operation"

st.write(f"Result: {result}")
