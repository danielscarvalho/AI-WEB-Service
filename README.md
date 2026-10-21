# AI-WEB-Service
AI WEB SERVICES - AI LLM and AI ML

This Python service exposes a Scikit-Learn Iris classifier through a Flask API.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

The service listens on `http://localhost:5000`. Check its status with
`GET /health` and send a prediction with `POST /predict`:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

`features` must contain four finite numbers in the order sepal length, sepal
width, petal length, and petal width (centimeters). A successful response
contains the predicted class ID and Iris species name.

## Run with Docker

```bash
docker build -t ai-web-service .
docker run --rm -p 5000:5000 ai-web-service
```

## Run tests

```bash
python -m unittest discover -s tests
```
