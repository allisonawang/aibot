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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Use pastel colors
    pastel_colors = ['#FF6666', '#BFBFBF', '#66FF66']
    
    # Create a horizontal bar chart with pastel colors and thinner bar lines
    ax1.barh(labels, percentages, color=pastel_colors, linewidth=0.5)
    
    # Display percentages on the bars
    for i, v in enumerate(percentages):
        ax1.text(v + 0.01, i, f'{v*100:.1f}%', color='black', va='center', fontweight='bold')

    ax1.set_xlabel('Percentage')
    ax1.set_title('Sentiment Analysis')

    # Add ASCII art for each sentiment category
    art_negative = """
    (ㅠ﹏ㅠ)
    """
    art_neutral = """
    -----
    ._.
    """
    art_positive = """
    \(◦'⌣'◦)/
    """

    # Display ASCII art based on sentiment
    ax2.set_title('Art')
    if sentiment_result['sentiment']['negative'] > 0.5:
        ax2.text(0.5, 0.5, art_negative, fontsize=20, ha='center', va='center')
    elif sentiment_result['sentiment']['positive'] > 0.5:
        ax2.text(0.5, 0.5, art_positive, fontsize=20, ha='center', va='center')
    else:
        ax2.text(0.5, 0.5, art_neutral, fontsize=20, ha='center', va='center')

    ax2.axis('off')

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

