import langchain_helper as lch
import streamlit as st

st.title("Pet name generator")

user_animal_type = st.sidebar.selectbox("What is your pet",("Dog","Cat"))
if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area("What color is your dog?", 
                                     max_chars=20)
    
if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area("What color is your cat?", 
                                     max_chars=20)


if user_pet_color:
    response = lch.generate_pet_name(user_animal_type,user_pet_color)
    st.text(response['pet_name'])