import random
import json
from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)

@app.route('/')
def users_page():
    return render_template('index.html')

@app.route('/uni')
def show_best_unis():
    return render_template('universities.html')

@app.route('/subjects')
def show_subjects():
    return render_template('subjects.html')

@app.route('/pc_free_certificates')
def pc_free_certificates():
    return render_template('pc_free_certificates.html')


if __name__ == "__main__":
    app.run(debug=True)
