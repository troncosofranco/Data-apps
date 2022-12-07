from flask import Flask, jsonify, request, render_template 
import json
from transformers import pipeline
import re

#define template folder
app = Flask(__name__, template_folder='templates')

summarizer = pipeline("summarization")

#define route for home page
@app.route('/')
def home():
    return render_template('index.html')

#route for UI (user interface)
@app.route('/prediction', methods = ["POST"])
def prediction():
    """
    This function takes a JSON with two fields: "text" and "maxlen"
    Returns: the summarized text of the paragraphs.
    """
    
     
    print(request.form.values())
    
    #get values from HTML form
    paragraphs = request.form.get("paragraphs")

    #replace enter by empty string
    paragraphs = re.sub("\d+", "", paragraphs)
    maxlen = int(request.form.get("maxlen"))

    summary = summarizer(paragraphs, max_length=maxlen, min_length=49, do_sample=False)
    return render_template('index.html', prediction_text = '" {} "'.format(summary[0]["summary_text"])), 200

#Define route for the API
@app.route('/api/prediction', methods = ["POST"])
def api_prediction():
    """
    This function takes a JSON with two fields: "text" and "maxlen"
    Returns: the summarized text of the paragraphs.
    """
    query = json.loads(request.data)
    paragraphs = re.sub("\d+", "", query["text"])
    maxlen = query["maxlen"]
    minlen = query["minlen"]
    summary = summarizer(paragraphs, max_length=maxlen, min_length=minlen, do_sample=False)
    return jsonify(summary), 200

if __name__ == '__main__':
    app.run(debug=False)










