import math
from numbers import Real

from flask import Flask, jsonify, request
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

iris = load_iris()
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
model.fit(iris.data, iris.target)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True)
    features = payload.get("features") if isinstance(payload, dict) else None
    if (
        not isinstance(features, list)
        or len(features) != 4
        or any(
            isinstance(value, bool)
            or not isinstance(value, Real)
            or not math.isfinite(value)
            for value in features
        )
    ):
        return jsonify(
            {"error": "features must be a list of four finite numbers"}
        ), 400

    class_id = int(model.predict([features])[0])
    return jsonify(
        {
            "prediction": {
                "class_id": class_id,
                "class_name": iris.target_names[class_id],
            }
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
