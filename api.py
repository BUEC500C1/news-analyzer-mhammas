from flask import Flask, escape, render_template, request
from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/create', methods = ['POST'])
def create_file():
    #name = request.args.get("file")
    f = request.files['file']
    return create(f)

@app.route('/delete')
def delete_file():
    name = request.args.get("file")
    return delete(name)

@app.route('/update')
def update_file():
    name = request.args.get("file")
    text = request.args.get("text")
    return update(name, text)

@app.route('/sentiment')
def calculate_sentiment():
    text = request.args.get("text")
    return get_sentiment(text)

@app.route('/keyword_search')
def keyword_search():
    keyword = request.args.get("keyword")
    return search_by_keyword(keyword)