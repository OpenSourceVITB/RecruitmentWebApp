# Author: VintellX
# Date: 24/01/2024
# Version: 0.0.1


# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD


from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

