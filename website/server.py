import random
import json
from flask import Flask, render_template, request, redirect, session 
from scripts import scrapeimg

app = Flask(__name__)

@app.route('/')
def users_page():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
