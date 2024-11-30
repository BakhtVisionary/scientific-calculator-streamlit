import streamlit as st
import math

# Streamlit App Title
st.title("Scientific Calculator")

# Input Fields
st.write("## Input your values:")
num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number (if applicable):", value=0.0, format="%.2f")

# Operation Selection
st.write("## Choose an operation:")
operation = st.selectbox(
    "Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Sine",
        "Cosine",
        "Tangent",
        "Logarithm (base 10)",
        "Natural Logarithm (ln)",
    ]
)

# Perform Calculations
result = None
try:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")
    elif operation == "Power":
        result = math.pow(num1, num2)
    elif operation == "Square Root":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            st.error("Square root of negative numbers is not supported.")
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
    elif operation == "Logarithm (base 10)":
        if num1 > 0:
            result = math.log10(num1)
        else:
            st.error("Logarithm is not defined for non-positive numbers.")
    elif operation == "Natural Logarithm (ln)":
        if num1 > 0:
            result = math.log(num1)
        else:
            st.error("Natural logarithm is not defined for non-positive numbers.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Display Result
if result is not None:
    st.write("## Result:")
    st.success(result)

# Additional Note
st.write("### Note:")
st.info("For trigonometric operations, the input angle is assumed to be in degrees.")
