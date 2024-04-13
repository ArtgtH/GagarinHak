from fastapi import FastAPI, File, UploadFile

import cv2


app = FastAPI()


def write_file(file):
	with open(f'{file.filename}', 'wb') as new_file:
		new_file.write(file.file.read())
	return 'success'


def img_test(img):
	print(img.shape)


@app.post("/api/detect")
async def detect(file: UploadFile):

	write_file(file)
	image = cv2.imread(file.filename)

	return {"message": "success", "mode": "classic"}


@app.post("/api/detect_extended")
async def detect_extended(file: UploadFile):

	write_file(file)
	image = cv2.imread(file.filename)

	return {"message": "success", "mode": "extended"}


if __name__ == '__main__':
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8000)
