# Project Description
Our project will focus on lowering the gender biases existing in the field of medicine through the use of AI, as a lot of existing research on health and the human body focuses on males [4]. 
The project will act as an AI assistant which works on top of existing AI systems to filter out gender biases towards women. 

# Features
- Upload `.txt` dataset files 
- Automatically scan and chunk dataset text 
- Label chunks as safe, flagged, or blocked 
- Ask questions against the uploaded dataset 
- Retrieve relevant chunks based on the query 
- Filter unsafe chunks before sending context to the LLM 
- View processed chunk summaries


# Installation
pip install google-generativeai
pip install flask
python -m pip install google-genai python-dotenv

# Files
- app.py : Flask application 
- guards.py : 
- llm_utils.py : 
- retriever.py : 
- scanner.py : 
- scoring.py : 
- index.html : 
- sample_data.txt : 
- readme.txt : 



