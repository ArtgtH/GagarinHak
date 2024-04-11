FROM python:3.11-slim

WORKDIR /api

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN apt-get update && pip install -r requirements.txt && apt-get install -y libgl1-mesa-glx && apt-get install -y libglib2.0

COPY . .

RUN rm ./requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]