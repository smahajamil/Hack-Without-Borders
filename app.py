#Flask application entry point.

#Endpoints:
  #POST /upload  - Upload a .txt dataset file; scan and store chunks.
  #POST /ask     - Ask a question; retrieve safe chunks and get an LLM answer.


from flask import Flask, request, jsonify, render_template
from scanner import scan_text
from retriever import retrieve_relevant_chunks
from guards import filter_chunks
from llm_utils import ask_llm

app = Flask(__name__)

# Store processed chunks (reset on each upload)
chunk_store: list[dict] = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    #Accept a .txt file upload, scan it for bias, and store the results.
    
    if "file" not in request.files:
        return jsonify({"error": "No file provided. Send a .txt file as 'file'."}), 400

    uploaded_file = request.files["file"]

    if not uploaded_file.filename.endswith(".txt"):
        return jsonify({"error": "Only .txt files are supported."}), 400

    raw_text = uploaded_file.read().decode("utf-8")

    if not raw_text.strip():
        return jsonify({"error": "Uploaded file is empty."}), 400

    global chunk_store
    chunk_store = scan_text(raw_text)

    # Build a summary of chunk statuses for the response
    status_summary = {"safe": 0, "flagged": 0, "blocked": 0}
    for chunk in chunk_store:
        status_summary[chunk["status"]] += 1

    return jsonify({
        "message": "Dataset processed successfully.",
        "chunks_processed": len(chunk_store),
        "status_summary": status_summary,
    })


@app.route("/ask", methods=["POST"])
def ask():
 
    #Accept a question, retrieve relevant chunks, filter biased ones, and return an LLM-generated answer.

    if not chunk_store:
        return jsonify({"error": "No dataset uploaded yet. POST to /upload first."}), 400

    body = request.get_json(silent=True)
    if not body or "question" not in body:
        return jsonify({"error": "Request body must include a 'question' field."}), 400

    question = body["question"].strip()
    if not question:
        return jsonify({"error": "Question cannot be empty."}), 400

    # 1. Retrieve the most relevant chunks by keyword overlap
    relevant_chunks = retrieve_relevant_chunks(question, chunk_store)

    # 2. Filter out blocked chunks (keep flagged by default)
    approved_chunks, blocked_ids = filter_chunks(relevant_chunks, allow_flagged=True)

    # 3. Ask the LLM using only approved context
    answer = ask_llm(question, approved_chunks)

    return jsonify({
        "answer": answer,
        "sources_used": [c["chunk_id"] for c in approved_chunks],
        "chunks_blocked": blocked_ids,
    })


@app.route("/chunks", methods=["GET"])
def list_chunks():
    
    if not chunk_store:
        return jsonify({"error": "No dataset uploaded yet."}), 400

    summary = [
        {
            "chunk_id": c["chunk_id"],
            "status": c["status"],
            "bias_score": c["bias_score"],
            "preview": c["text"][:80] + ("..." if len(c["text"]) > 80 else ""),
        }
        for c in chunk_store
    ]
    return jsonify({"chunks": summary})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
