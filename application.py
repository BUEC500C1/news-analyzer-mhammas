from flask import Flask, escape, render_template, request
from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def main():
   return render_template('main.html')

@application.route('/upload')
def upload():
   return render_template('upload.html')

@application.route('/read')
def read():
    return read_records()

@application.route('/create', methods = ['POST'])
def create_file():
    #name = request.args.get("file")
    f = request.files['file']
    return create(f)

@application.route('/delete')
def delete_file():
    name = request.args.get("file")
    return delete(name)

@application.route('/update')
def update_file():
    name = request.args.get("file")
    text = request.args.get("text")
    return update(name, text)

@application.route('/sentiment')
def calculate_sentiment():
    text = request.args.get("text")
    return get_sentiment(text)

@application.route('/entities')
def calculate_entities():
    text = request.args.get("text")
    return get_entities(text)

@application.route('/entitysentiment')
def calculate_entitysentiment():
    text = request.args.get("text")
    return get_entities_and_sentiment(text)

@application.route('/keyword_search')
def keyword_search():
    keyword = request.args.get("keyword")
    return search_by_keyword(keyword)

if __name__ == "__main__":
    application.run(debug=True)