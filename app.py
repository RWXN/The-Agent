import streamlit as st
from workflow import execute_workflow

col1_header_1, col2_header_2 = st.columns([0.15, 0.35])  
with col1_header_1:
    st.header("Welcome!!!")
with col2_header_2:
    hello_image_url = "https://cromsalvatera.com.au/wp-content/uploads/2024/11/Agent-AI.webp"  
    st.image(hello_image_url, width=100) 

st.write("I am a senior AI agent ready to assist you in answering your inquires.")
quiry = st.text_area("Please enter your inquiry here: ")

search_button = st.button("search")
if search_button:
    with st.spinner("Processing your inquiry..."):
        response = execute_workflow(quiry)

    if isinstance(response, dict) and len(response) >= 2:
        if response["code"] == 200:
            st.write(response["message"])
        elif response["code"] == 400:
            st.write(response["message"])
    else:
        st.warning("Sorry, your inquiry could not be able to processed at this time. Please retry later.")


