# Author: VintellX
# Date: 24/01/2024
# Version: 0.0.1


# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD


from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from pymongo import MongoClient
import os
from xDmongo import importo
import re
import redis

app = Flask(__name__)
xdsecret: str= os.urandom(24).hex()
app.secret_key = xdsecret 
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'trasho_'
rediso: str= os.environ.get('REDIS_URI')
redisp: str= os.environ.get('REDIS_PASS')
redisport: int= os.environ.get('REDIS_PORT')
app.config['SESSION_REDIS'] = redis.Redis(host=rediso,port=redisport,password=redisp)
Session(app)

# Initialize MongoDB
MONGO_URI: str= os.environ.get('MONGO_URI')
wtf = MongoClient(MONGO_URI)
db = wtf.xData
recruit = db.recruit

from prototype import UserData

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recruitment')
def recruit():
    return render_template('recruitment.html')

@app.route('/recruitment/process', methods=['GET','POST'])
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
        status = 'Confirmed'
        log = "Thanks for the initiative and yours' interest."
        session.clear()
        session['name'] = name
        session['status'] = status
        session['log'] = log
        if not re.search(r'@vitbhopal\.ac\.in$', email):
            session['status'] = 'Failed!'
            session['log'] = 'Please enter a valid VIT Bhopal email address!'
            return redirect(url_for('submission'))
        if not re.search(r'^[0-9]{10}$', phone):
            session['status'] = 'Failed!'
            session['log'] = 'Please enter a valid phone number!'
            return redirect(url_for('submission'))
        status = UserData.updato(name, email, regnum, phone, team, sellingpoint, linkedin, github, projectolink, resumelink, ques1, ques2, ques3)
        session['status'] = status
        return redirect(url_for('submission'))
    return render_template('form.html')

@app.route('/recruitment/submission')
def submission():
    name = session.get('name') or None
    status = session.get('status') or None
    log = session.get('log') or None
    print(name, status, log)
    return render_template('submission.html', name=name, status=status, log=log) if name else redirect(url_for('recruit'))
