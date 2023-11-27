import streamlit as st
import requests
from app.komprehend import getSentiment


st.title("Sentiment Analyzer")
user_input = st.text_input("Enter a sentence: ")

if st.button("Analyze Sentiment"):
        # Check if the user has entered text
        if user_input:
            # Use the Komprehend API to analyze sentiment
            sentiment_result = getSentiment(user_input)
            # Display the result
            st.write(f"Sentiment: {sentiment_result}")
        else:
            st.warning("Please enter a sentence.")