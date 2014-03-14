from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template


app = Flask(__name__)
app.config.from_object(__name__)
@app.route('/')
def index():
	return render_template('index.html')

if __name__ ==  '__main__': 
	app.debug=True
	app.run()