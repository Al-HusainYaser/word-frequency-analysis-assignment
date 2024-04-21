FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install nltk
RUN python -m nltk.downloader punkt stopwords

CMD ["python", "./DockerAssignment.py"]