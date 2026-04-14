class MLSignalFilter:
    """
    Filters strategy signals using ML predictions
    """

    def __init__(self, model, threshold=0.6):
        self.model = model
        self.threshold = threshold

    def filter(self, features, signal):

        prob = self.model.predict_proba(features)[-1]

        if signal.signal_type == "LONG" and prob > self.threshold:
            return signal

        elif signal.signal_type == "SHORT" and prob < (1 - self.threshold):
            return signal

        else:
            return None