import streamlit as st 
import beginner
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian","Pakistani","American","English","Chinese","Russian","Italian","Mexican"))

if cuisine:
    response = beginner.generate_restaurant_name(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write("--", item)
