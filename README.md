# Hack-Without-Borders
AI Bias Detection and Data Filtering System

# Project Description
Our project will focus on lowering the gender biases existing through the use of AI to bridge the digital divide of data visibility. 
The project will act as an  which works on top of existing AI systems to filter out gender biases towards women. 

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
- app.py : Flask application entry point. Upload a .txt dataset file; scan and store chunks. Ask a question; retrieve safe chunks and get an LLM answer.
- guards.py : Filters retrieved chunks before they are sent to the LLM by removing blocked content, optionally excluding flagged content, and returning both the approved chunks and the IDs of blocked ones.
- llm_utils.py : Loads the Google Gemini API key, sends the user’s question and provided context to the Gemini model, and returns an answer based only on that context.
- retriever.py : Finds the most relevant chunks for a user question using simple keyword overlap scoring. Count how many question words appear in the chunk. Rank all chunks by keyword relevance to the question.
- scanner.py : Split text into chunks and score each for bias. Returns a list of chunk dicts with id, text, bias_score, and status.
- scoring.py : Assigns a bias score to a text chunk using general rules. Bias score thresholds: 0 → safe, 2 → flagged, 3+  → blocked
- index.html : Main website document.
- sample_data.txt : Sample dataset file for demo.

# References
Flask Documentation
https://flask.palletsprojects.com/en/stable/

Flask JSON API Guide
https://flask.palletsprojects.com/en/stable/quickstart/#apis-with-json

Flask Request Handling
https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data

Python Regex Documentation (W3Schools)
https://www.w3schools.com/python/python_regex.asp

JavaScript JSON Documentation
https://www.w3schools.com/js/js_json.asp

Stack Overflow – Sending Data Between Python and JavaScript
https://stackoverflow.com/questions/59149354/how-to-send-data-from-python-script-to-javascript-and-vice-versa

Google Gemini API Authentication Documentation
[https://docs.cloud.google.com/docs/authentication/api-keys](https://ai.google.dev/gemini-api/docs/api-key)


# Citations (for all project documents)
[1]	IEEE Xplore, “Male‑dominated STEM disciplines: How do we make them more attractive to
women?” Accessed: March 14, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/8360911
[2] 	UNESCO, “Generative AI: UNESCO study reveals alarming evidence of regressive gender
stereotypes.” Accessed: March 14, 2026. [Online]. Available: https://www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes
[3] 	S. Liss, “Changes coming to women’s health research traditionally based on males.”
Accessed: March 14, 2026. [Online]. Available: https://innovationfactory.ca/changes-coming-to-womens-health-research-traditionally-based-on-males/
[4] 	BBC Future, “How gender bias affects your healthcare.” Accessed: March 14, 2026. [Online].
Available: https://www.bbc.com/future/article/20180523-how-gender-bias-affects-your-healthcare
[5] 	UN Women, “How AI reinforces gender bias and what we can do about it.” Accessed: March
14, 2026. [Online]. Available: https://www.unwomen.org/en/news-stories/interview/2025/02/how-ai-reinforces-gender-bias
and-what-we-can-do-about-it
[6]	Massive Bio, “Panacea.” Accessed: March 15, 2026. [Online]. Available:
https://massivebio.com/panacea-bio/ 
[7]	Google Cloud, “API keys authentication.” Accessed: March 15, 2026. [Online]. Available:
https://docs.cloud.google.com/docs/authentication/api-keys
[8] 	W3Schools, “Python Regex.” Accessed: March 15, 2026. [Online]. Available:
https://www.w3schools.com/python/python_regex.asp
[9] 	Pallets, “Flask API documentation.” Accessed: March 15, 2026. [Online]. Available:
https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify
[10] 	Pallets, “Flask Quickstart – Accessing request data.” Accessed: March 15, 2026. [Online].	Available: https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data
[11] 	Pallets, “Flask Quickstart – APIs with JSON.” Accessed: March 15, 2026. [Online].
Available: https://flask.palletsprojects.com/en/stable/quickstart/#apis-with-json
[12] 	Python Advanced Web Apps, “Flask web applications.” Accessed: March 15, 2026. [Online].
Available: https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
[13] 	Stack Overflow, “How to send data from Python script to JavaScript and vice versa.”
Accessed: March 15, 2026. [Online]. Available:
https://stackoverflow.com/questions/59149354/how-to-send-data-from-python-script-to-javacript-and-vice-versa
[13] 	W3Schools, “JavaScript JSON.” Accessed: March 15, 2026. [Online]. Available:
https://www.w3schools.com/js/js_json.asp
[14] 	T. Bolukbasi, K.-W. Chang, J. Zou, V. Saligrama, and A. Kalai, “Man is to computer
programmer as woman is to homemaker? Debiasing word embeddings,” 2016. Accessed:
March 15, 2026. [Online]. Available: https://web.cs.ucla.edu/~kwchang/bibliography/bolukbasi2016man/
[15]	ChatGPT, response to prompt “How to code front-end JavaScript for chat UI” version 5.3,
OpenAI, March 15, 2026. Accessed: March 15, 2026.
[16]	Criado-Perez, Caroline. “The Deadly Truth about a World Built for Men – from Stab Vests to Car Crashes.” The Guardian, 23 Feb. 2019, www.theguardian.com/lifeandstyle/2019/feb/23/truth-world-built-for-men-car-crashes
[17]	Marwala, Tshilidzi. “The Digital Divide Is Not Just Access. It Is Also Visibility.” United Nations University, 2026, unu.edu/article/digital-divide-not-just-access-it-also-visibility Accessed 15 Mar. 2026.
[18]	O’Hagan, Clare. “Generative AI: UNESCO Study Reveals Alarming Evidence of Regressive Gender Stereotypes.” Unesco.org, 2019, www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes

