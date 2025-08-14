import streamlit as st 
import helper

st.title("Resturant Name Generator")
cusine=st.sidebar.selectbox("pick a cusine ",("india","arabic","america","china","japan","andhrapradesh")) 


    
if cusine:
    response=helper.generte_resturant_itmes(cusine)
    st.header(response['restaurant_name'].strip()) 
    menu_items=response['items'].strip().split(",")
    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write(item)