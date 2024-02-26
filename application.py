from flask import Flask, escape, render_template, request, redirect, url_for, session
from NewsfeedIngestor.ingestor import * # import functions from other files
from SecureFileUploader.uploader import * # import functions from other files
from TextNLPAnalysis.nlp import * # import functions from other files

application = Flask(__name__)
application.secret_key = 'ADD_SECRET_KEY_HERE'

@application.route('/')
@application.route('/index')
def index():
   return render_template('signup.html')

@application.route('/signup')
def signup():
   return render_template('signup.html')

@application.route('/login')
def login():
   return render_template('login.html')

@application.route('/signup_post', methods = ['POST'])
def signup_post():
    name = request.form.get("name")
    password = request.form.get("password")
    retVal = signup_user(name, password)
    if retVal['status'] == 200:
        return redirect(url_for('login_post'), code=307)
    else:
        return redirect(url_for('signup'))

@application.route('/login_post', methods = ['POST'])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")
    retVal = login_user(name, password)
    if retVal['status'] == 200:
        session['username'] = name
        return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))

@application.route('/main')
def main():
    if 'username' in session:
        return render_template('main.html')
    else:
        return redirect(url_for('index'))

@application.route('/logout')
def logout():   
    session.pop('username', default=None)
    return redirect(url_for('index'))

@application.route('/upload')
def upload():
   return render_template('upload.html')

@application.route('/read')
def read():
    docs = read_records(session['username'])
    return render_template('records.html', docs=docs)

@application.route('/create', methods = ['POST'])
def create_file():
    #name = request.args.get("file")
    f = request.files['file']
    return create(session['username'], f)

@application.route('/delete')
def delete_file():
    username = request.args.get("username")
    filename = request.args.get("filename")
    return delete(username, filename)

@application.route('/update')
def update_file():
    name = request.args.get("file")
    text = request.args.get("text")
    return update(name, text)

@application.route('/sentiment')
def sentiment():
   return render_template('sentiment.html')


@application.route('/sentiment/get_sentiment')
def calculate_sentiment():
    text = request.args.get("text")
    sentiment = get_sentiment(text)["sentiment"]
    return render_template('sentiment.html', sentiment=sentiment)

@application.route('/sentiment/get_entities')
def calculate_entities():
    text = request.args.get("text")
    return get_entities(text)

@application.route('/sentiment/get_entitysentiment')
def calculate_entitysentiment():
    text = request.args.get("text")
    return get_entities_and_sentiment(text)

@application.route('/search')
def search():
   return render_template('search.html')


@application.route('/search/keyword_search')
def keyword_search():
    keyword = request.args.get("keyword")
    articles = search_by_keyword(keyword)["articles"]
    return render_template('search.html', articles=articles)

if __name__ == "__main__":
    application.run(debug=True)
