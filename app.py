from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', data = {'name':'HEY'})

@app.route('/<name>', methods=['GET'])
def shutup(name):
  return render_template('index.html', data = {'name':name.upper()})