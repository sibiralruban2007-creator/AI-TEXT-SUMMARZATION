# AI-TEXT-SUMMARZATION
🤖 AI Text Summarizer
📌 About the Project

The AI Text Summarizer is an AI-powered web application that summarizes long text into a shorter and meaningful version using a pretrained Transformer-based language model, Hugging Face Transformers, and Streamlit.

The application provides a simple and user-friendly interface where users can enter or paste a long paragraph, click the Summarize Text button, and view the generated summary.

✨ Features
📝 User-friendly text input
🤖 AI-powered text summarization
🧠 Uses a pretrained Transformer model
⚡ Fast and simple summarization
🖥️ Interactive Streamlit interface
📄 Summarizes long paragraphs
📊 Displays the generated summary clearly
🚫 Shows a warning when no text is provided
🔄 Generates concise summaries automatically
🛠️ Technologies Used
Technology	Purpose
Python	Application development
Streamlit	Web application interface
Hugging Face Transformers	AI model and text summarization
PyTorch	Deep learning framework
Transformer Model	Text summarization
GitHub	Version control and project hosting
🧠 AI Model

This project uses a pretrained Transformer-based summarization model from Hugging Face.

Model Details
Parameter	Details
Model	facebook/bart-large-cnn
Developer	Meta AI
Architecture	Transformer
Task	Text Summarization
Library	Hugging Face Transformers

The BART model is designed for sequence-to-sequence tasks and can generate concise summaries from longer text.

🔄 How It Works

The application follows a simple AI text summarization workflow:

User Input
    ↓
Streamlit Application
    ↓
Hugging Face Pipeline
    ↓
BART Transformer Model
    ↓
Text Summarization
    ↓
Generated Summary
    ↓
Display to User
🔹 Workflow Steps
User Input – The user enters or pastes a long paragraph.
Streamlit Application – The application receives the input text.
Hugging Face Pipeline – The text is passed to the summarization pipeline.
BART Model – The pretrained model processes the input.
Text Summarization – The model generates a shorter version of the text.
Generated Summary – The summary is displayed to the user.
📸 Application Preview
The Streamlit application provides a simple interface where users can:
<img width="1016" height="716" alt="image" src="https://github.com/user-attachments/assets/ede0e39e-9fb7-4459-a3aa-474cee53642d" />
🧪 Example
Input
Artificial Intelligence is a rapidly developing technology that
enables computers and machines to perform tasks that normally
require human intelligence. AI is used in many areas such as
healthcare, education, transportation, finance, and communication.
It helps organizations analyze data, automate tasks, and make
better decisions.
Generated Output
Artificial Intelligence enables machines to perform tasks
requiring human intelligence and is widely used in areas
such as healthcare, education, transportation, and finance.


📁 Project Structure
AI-Text-Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
