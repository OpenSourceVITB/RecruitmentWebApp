# Author: VintellX
# Date: 24/01/2024
# Version: 0.0.1


# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD


from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from pymongo import MongoClient
import os
from prototype import UserData

app = Flask(__name__)

# Initialize MongoDB
MONGO_URI: str= os.environ.get('MONGO_URI')
wtf = MongoClient(MONGO_URI)
db = wtf.xData
recruit = db.recruit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recruitment')
def recruit():
    return render_template('recruitment.html')

@app.route('/recruitment/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        regnum = request.form['regnum']
        phone = request.form['phone']
        team = request.form['team']
        sellingpoint = request.form['sellingpoint']
        linkedin = request.form['linkedin']
        github = request.form['github']
        projectolink = request.form['projectolink']
        resumelink = request.form['resumelink']
        ques1 = request.form['ques1']
        ques2 = request.form['ques2']
        ques3 = request.form['ques3']
        xd = UserData.updato(name, email, regnum, phone, team, sellingpoint, linkedin, github, projectolink, resumelink, ques1, ques2, ques3)

@app.route('/recruitment/submission')
def submission():
    pass

if __name__ == '__main__':
    app.run(debug=True)
