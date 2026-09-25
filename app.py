```python
import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="",
    layout="centered"
)

# Application title
st.title(" AI Text Summarizer")
st.write("Summarize text using the BART Large CNN model.")

# Load the model only once
@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    return summarizer

# Load model
with st.spinner("Loading AI model..."):
    summarizer = load_model()

# User input
text = st.text_area(
    "Enter your text:",
    placeholder="Paste the text you want to summarize here...",
    height=250
)

# Summarize button
if st.button(" Summarize Text"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            result = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )

        summary = result[0]["summary_text"]

        st.subheader(" Summary")
        st.write(summary)

# Footer
st.markdown("---")
st.caption("Powered by BART Large CNN | Hugging Face Transformers | Streamlit")
```

