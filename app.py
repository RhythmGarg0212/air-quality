# Create a Streamlit app for the user interface
import streamlit as st
import pickle
st.title("Air Quality Index Prediction")
st.write("Enter the required details to predict the Air Quality Index.")

No2 = st.text_input("Enter NO2 amount")
So2 = st.text_input("Enter SO2 amount")
rspm=st.text_input("Enter rspm amount")
spm=st.text_input("Enter spm amount")

if st.button("Predict"):
    # Load the trained model
    with open('air_quality_modeln.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    
    # Create a feature vector using user input
    user_input = [No2,So2,rspm,spm]  # Add more features if needed

    # Make a prediction
    prediction = loaded_model.predict([user_input])

    st.write(f"Predicted Air Quality Index for Given conditions is : {prediction[0]}")

    
