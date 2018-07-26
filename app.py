"""Main module for running the application"""

# !/usr/bin/python'
from flask import Flask, request, render_template
from utils.make_sql_file import make_file
from utils.directory_validator import validate_directory_exists


def run():
    """
    generates the app
    :return: app
    """
    flask_app = Flask(__name__)
    return flask_app


validate_directory_exists()
app = run()


@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    """
    Handles the request as a form
    :return: template for download if POST or template for index if GET
    """
    if request.method == 'POST':
        startday = request.form['startday']
        endday = request.form['endday']
        make_file(startday, endday)
        return render_template('result.html')

    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def page():
    """
    Sends the index page for root of the applicaiton
    :return: index.html
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988, debug=True)
