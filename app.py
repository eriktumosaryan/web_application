#!/usr/bin/python3
from flask import Flask, render_template, url_for

import json 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

@app.route('/home')
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about_us')
def show_about():
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
if __name__ == "__main__":
    app.run(debug=True, port="8000")
