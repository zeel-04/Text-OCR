import streamlit as st  #Web App

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg",width=200)

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg",width=200)

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg",width=200)