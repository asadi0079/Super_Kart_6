
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("SuperKart_Rev_prediction_model_v1_0.joblib")

model = load_model()

# Streamlit UI for Price Prediction
st.title("SuperKart Rev Predictor")
st.write("This tool predicts the rev per store per product.")

st.subheader("Enter the store details:")

# Collect user input
StoreID = st.selectbox("Store_ID", ["OUT001", "OUT002", "OUT003", "OUT004"])
StoreSize = st.selectbox("Store Size", ["Small", "Medium", "High"])
StoreLocationCityType = st.selectbox("City Type", ["Tier 1", "Tier 2", "Tier 3"])
StoreType = st.selectbox("Store Type", ["Departmental", "Supermarket Type 1", "Supermarket Type 2"])
StoreYear = st.number_input("Store est year")
ProductID = st.text_input("Product_ID")
ProductType = st.selectbox("Product Type", ["Fruits and Vegetables", "Snack Foods", "Frozen Foods", "Dairy", "Household", "Baking Goods", "Canned", "Health and Hygiene", "Meat", "Soft Drinks", "Bread", "Hard Drinks", "Others", "Starchy Foods","Breakfast","Seafood" ])
Product_Sugar_Content = st.selectbox("Product Sugar Content if applicable", ["Low Sugar", "Regular", "No Sugar"])

ProductWeight = st.number_input("Product Weight")
ProductAllocatedArea = st.number_input("Product Allocated Area")
ProductMRP = st.number_input("Product Price")


#accommodates = st.number_input("Accommodates (Number of guests)", min_value=1, value=2)
#bathrooms = st.number_input("Bathrooms", min_value=1, step=1, value=2)
#cancellation_policy = st.selectbox("Cancellation Policy (kind of cancellation policy)", ["strict", "flexible", "moderate"])
#cleaning_fee = st.selectbox("Cleaning Fee Charged?", ["True", "False"])
#instant_bookable = st.selectbox("Instantly Bookable?", ["False", "True"])
#review_scores_rating = st.number_input("Review Score Rating", min_value=0.0, max_value=100.0, step=1.0, value=90.0)
#bedrooms = st.number_input("Bedrooms", min_value=0, step=1, value=1)
#beds = st.number_input("Beds", min_value=0, step=1, value=1)

# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'Store_Id': StoreID,
    'Store_Size': StoreSize,
    'Store_Location_City_Type': StoreLocationCityType,
    'Store_Type': StoreType,
    'Store_Establishment_Year': StoreYear,
    'Product_Id': ProductID,
    'Product_Type': ProductType,
    'Product_Sugar_Content': Product_Sugar_Content,
    'Product_Weight': ProductWeight,
    'Product_Allocated_Area': ProductAllocatedArea,
    'Product_MRP': ProductMRP,
  
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"The predicted revenue for the product at the store is ${np.exp(prediction)[0]:.2f}.")
