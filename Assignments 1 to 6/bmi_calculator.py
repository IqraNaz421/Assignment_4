import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_in_feet):
    # Convert height from feet to meters
    height_in_meters = height_in_feet * 0.3048
    # Calculate BMI using the formula
    bmi = weight / (height_in_meters ** 2)
    return bmi

# Function to provide BMI category based on BMI value
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit UI
st.title("BMI Calculator")

# Take user input for weight (in kg) and height (in feet)
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height_in_feet = st.number_input("Enter your height (feet):", min_value=0.1)

# Ensure both inputs are valid
if weight > 0 and height_in_feet > 0:
    # Calculate BMI
    bmi = calculate_bmi(weight, height_in_feet)
    
    # Get the BMI category
    bmi_category = get_bmi_category(bmi)
    
    # Display the result
    st.write(f"Your BMI is: {bmi:.2f}")
    st.write(f"Your BMI category is: {bmi_category}")
    
    # Additional health advice based on BMI category
    if bmi_category == "Underweight":
        st.warning("You may need to gain some weight. Please consult a healthcare provider.")
    elif bmi_category == "Normal weight":
        st.success("You are in a healthy weight range. Keep up the good work!")
    elif bmi_category == "Overweight":
        st.warning("You may need to lose some weight. Please consult a healthcare provider for advice.")
    else:
        st.error("You may need to lose a significant amount of weight. Please consult a healthcare provider.")

else:
    st.error("Please enter valid weight and height values.")
