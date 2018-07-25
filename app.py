#!/usr/bin/python'
from utils.warninggenerator import warning_generator
from flask import Flask, request, Response, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        startday = request.form['startday']
        endday = request.form['endday']
        make_file(startday, endday)
        # return send_from_directory('static/downloads', 'fakewarnings.sql')
        return render_template('result.html')
    else:
        return render_template('index.html')
    


@app.route('/')
def page():
    render_template('index.html')
        

def make_file(start, end):
    fo = open("static/downloads/fakewarnings.sql", "w+")

    sql_script = warning_generator(int(start), int(end))

    fo.write("%s" % sql_script)
    fo.close()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988, debug=True)
