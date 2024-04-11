from flask import Flask, render_template, request, jsonify

import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_form():
	return render_template('form.html')


@app.route('/', methods=['POST'])
def post_form():

	file = request.files['file']

	answer = requests.post('http://localhost:8000/api/model', files={'file': file})

	print(answer.json())

	context = {'answer': answer.text}

	return render_template('result.html', result=context)


@app.route('/about', methods=['GET'])
def get_about_us():
	return render_template('about_us.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555)
