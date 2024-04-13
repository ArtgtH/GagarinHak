from fastapi import FastAPI, File, UploadFile
from PIL import Image

from classificator import get_class_and_proba


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
	image = Image.open(file.filename).convert('RGB')
	res = get_class_and_proba(image)

	return {"message": "success", "result": res}


@app.post("/api/detect_extended")
async def detect_extended(file: UploadFile):
	write_file(file)
	image = Image.open(file.filename).convert('RGB')
	res = get_class_and_proba(image)

	return {"message": "success", "result": res}


if __name__ == '__main__':
	import uvicorn

	uvicorn.run(app, host="127.0.0.1", port=8000)
