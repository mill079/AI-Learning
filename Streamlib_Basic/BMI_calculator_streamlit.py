import streamlit as st

st.title("💪 This is an Awesome BMI Calculator!")

st.subheader("📏 Enter your weight in kg and height in feet")

# Inputs
height_input = st.text_input("Enter your Height (in feet): ")
weight_input = st.text_input("Enter your Weight (in kg): ")

calculate_btn = st.button("Calculate BMI")

if calculate_btn:
    try:
        height_ft = float(height_input)
        weight_kg = float(weight_input)

        if height_ft > 0 and weight_kg > 0:
            st.success("✅ Calculating BMI...")
            height_m = height_ft / 3.2808  # 1 ft = 0.3048 m, but dividing by 3.2808 is equivalent
            bmi = weight_kg / (height_m ** 2)
            bmi = round(bmi, 2)

            st.success(f"🎯 Your BMI is: {bmi}")

            # Classification
            if bmi < 16:
                st.error("🚨 Category: Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("⚠️ Category: Underweight")
            elif 18.5 <= bmi < 25:
                st.success("✅ Category: Healthy")
            elif 25 <= bmi < 30:
                st.info("ℹ️ Category: Overweight")
            else:
                st.error("🚨 Category: Extremely Overweight")
        else:
            st.error("❗ Please enter positive numbers for both height and weight.")

    except ValueError:
        st.error("❌ Invalid input! Please enter numeric values only.")
