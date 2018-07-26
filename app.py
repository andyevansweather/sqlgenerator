#!/usr/bin/python'
from utils.make_sql_file import make_file
from flask import Flask, request, render_template
import os

downloads_dir = 'static/downloads'

if not os.path.exists(downloads_dir):
    os.makedirs(downloads_dir)

app = Flask(__name__)

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        startday = request.form['startday']
        endday = request.form['endday']
        make_file(startday, endday)
        return render_template('result.html')
    else:
        return render_template('index.html')
    


@app.route('/', methods=['GET', 'POST'])
def page():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988, debug=True)
