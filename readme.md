# Next Research Direction - GitHub README.md
<br> demo : https://next-research-direction.streamlit.app/
## Introduction
"Next Research Direction" is an innovative Streamlit application that leverages Google's Generative AI to assist researchers in identifying future research directions based on their abstracts. This tool is designed to analyze scientific abstracts and provide insightful suggestions on potential research paths, along with relevant paper links for further exploration.

## Features
* Abstract Analysis: Input your research abstract to receive tailored research direction suggestions.
* AI-Powered Insights: Utilizes advanced AI models for deep understanding and context-aware recommendations.
* Relevant Resource Linking: Provides links to pertinent papers, aiding in literature review and idea expansion.
* User-Friendly Interface: Easy-to-use text area for abstract input and clear display of AI-generated suggestions.
## How to Use
1. Enter Your Abstract: Paste your research abstract into the provided text area.
2. Generate Suggestions: Click the 'Generate' button to process your abstract.
3. Review the Results: The application will display a list of possible research directions and relevant paper links based on the abstract.
## Installation
To use this application, ensure you have Streamlit and the Google Generative AI API set up:

    pip install streamlit
<br>

    pip install google.generativeai
Also, configure your Google Generative AI API key (on api.py files) as detailed in their documentation.

## Usage Example
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
    st.write('give me your abstract, ill help you to provide some insight of your next research direction')
    
    # Create a text input for the prompt
    prompt = st.text_area("Enter your abstract:")
  
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        response = genai.generate_text(
          **defaults,
          prompt=('Based on this abstract, give me the list of next research directions that I can do and explain. Also, give the paper link that is relevant to that suggestion. Abstract: ' + prompt)
        )
        st.write(response.result)
## Support
For support, questions, or contributions, please visit the GitHub repository and open an issue or pull request.

## License
This project is released under the MIT License. See the LICENSE file in the repository for more information.

# Unlock your research potential with "Next Research Direction"! 🔍📚🚀
