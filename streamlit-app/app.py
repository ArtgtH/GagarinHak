import streamlit as st
import requests


if __name__ == '__main__':

	st.title("Gagarin Hak")

	file = st.file_uploader("Выберите изображение", type=["jpg", 'png', 'jpeg'])

	if file:
		st.image(file)

		send = st.button("Отправить")

		if send:
			answer = requests.post('http://api:8000/api/model', files={'file': file})

			st.header(answer.text)
