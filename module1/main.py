from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets

tweet_template = "Give me {number} jokes on {topic} in {language} language"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic', 'language'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model


import streamlit as st

st.header("🐦 Ramesh Nookala - Joke Generator")

st.subheader("Generate Jokes using Generative AI 🤖")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

language_options = ["English", "Hindi", "Telugu"]
language = st.selectbox("Select a language:", language_options)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic, "language" : language})
    st.write(tweets.content)
    
