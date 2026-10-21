import unittest

from app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_predict(self):
        response = self.client.post(
            "/predict", json={"features": [5.1, 3.5, 1.4, 0.2]}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["prediction"],
            {"class_id": 0, "class_name": "setosa"},
        )

    def test_predict_rejects_invalid_features(self):
        for features in (
            [5.1, 3.5, 1.4],
            [5.1, 3.5, 1.4, float("nan")],
            [True, 3.5, 1.4, 0.2],
            "5.1,3.5,1.4,0.2",
        ):
            with self.subTest(features=features):
                response = self.client.post(
                    "/predict", json={"features": features}
                )

                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.get_json())

    def test_predict_rejects_missing_or_non_object_json(self):
        for body in (None, [], {"other": [5.1, 3.5, 1.4, 0.2]}):
            with self.subTest(body=body):
                response = self.client.post("/predict", json=body)

                self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
