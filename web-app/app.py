from flask import Flask, render_template, request, jsonify

import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_form():
	return render_template('form.html')


@app.route('/full_res', methods=['POST'])
def full_res():
	file = request.files['file']

	answer = requests.post('http://api:8000/api/detect_extended', files={'file': file})

	answer = answer.json().get('result')

	doc_type = answer[0]
	score = answer[1]

	return render_template('result.html', score=score, doc_type=doc_type)


@app.route('/res', methods=['POST'])
def res():

	file = request.files['file']

	answer = requests.post('http://api:8000/api/detect', files={'file': file})

	answer = answer.json().get('result')

	doc_type = answer[0]
	score = answer[1]

	return render_template('result.html', score=score, doc_type=doc_type)


@app.route('/about', methods=['GET'])
def get_about_us():
	return render_template('about_us.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555)
