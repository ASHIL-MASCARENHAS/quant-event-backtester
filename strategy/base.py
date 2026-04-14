from abc import ABC, abstractmethod
from ml import feature_pipeline


class Strategy(ABC):

    def __init__(self, data_handler, events, ml_filter=None, feature_pipeline=None):
        self.data_handler = data_handler
        self.events = events
        self.ml_filter = ml_filter
        self.feature_pipeline = feature_pipeline

    @abstractmethod
    def generate_signals(self, event):
        # After creating signal
        if self.ml_filter and self.feature_pipeline:

            features = self.feature_pipeline.transform(bars)

            if len(features) == 0:
                return

            filtered_signal = self.ml_filter.filter(features, signal)

            if filtered_signal:
                self.events.put(filtered_signal)

        else:
            self.events.put(signal)