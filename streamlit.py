import streamlit as st
import requests
from app.komprehend import getSentiment
import matplotlib.pyplot as plt
import numpy as np

def plot_sentiment_chart(sentiment_result):
    labels = ['Negative', 'Neutral', 'Positive']
    percentages = [sentiment_result['sentiment']['negative'],
                   sentiment_result['sentiment']['neutral'],
                   sentiment_result['sentiment']['positive']]

    fig, ax = plt.subplots()

    # Use pastel colors
    pastel_colors = ['#C40233', '#BDBABB', '#127852']
    
    # Create a horizontal bar chart with pastel colors
    ax.barh(labels, percentages, color=pastel_colors, linewidth=0.25)
    
    # Display percentages on the bars
    for i, v in enumerate(percentages):
        ax.text(v + 0.01, i, f'{v*100:.1f}%', color='black', va='center', fontweight='bold')

    ax.set_xlabel('Percentage')
    ax.set_title('Sentiment Analysis')

    st.pyplot(fig)

st.title("Sentiment Analyzer")
user_input = st.text_input("Enter a sentence: ")

if st.button("Analyze Sentiment"):
        # Check if the user has entered text
        if user_input:
            # Use the Komprehend API to analyze sentiment
            sentiment_result = getSentiment(user_input)
            # # Display the result
            # st.write(f"Sentiment: {sentiment_result}")
            # Plot sentiment chart
            plot_sentiment_chart(sentiment_result)
        else:
            st.warning("Please enter a sentence.")

