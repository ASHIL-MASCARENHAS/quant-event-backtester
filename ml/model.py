from sklearn.linear_model import LogisticRegression


class MLModel:

    def __init__(self):
        self.model = LogisticRegression()
        self.trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.trained = True

    def predict_proba(self, X):
        if not self.trained:
            raise ValueError("Model not trained")
        return self.model.predict_proba(X)[:, 1]