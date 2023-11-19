import streamlit as st
import google.generativeai as genai
from api import api

# Configure the API key
genai.configure(api_key=api)

# Set default parameters
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

st.title('Next Research Direction')
st.write('give me your abstract, ill help you to provide some insight of you next research direction')

# Create a text input for the prompt
prompt = st.text_area("Enter your abstract:")

# When the 'Generate' button is pressed, generate the text
if st.button('Generate'):
    response = genai.generate_text(
      **defaults,
      prompt=(('base on this abstract, give me the list of next research directions that i can do and explain. and also give the paper link that relevant on that suggestion. abstract: ' + prompt))
    )
    st.write(response.result)