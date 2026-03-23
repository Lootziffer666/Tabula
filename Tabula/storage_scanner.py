import os

class StorageScanner:
    def __init__(self, paths):
        self.paths = paths

    def scan(self):
        sizes = {}
        for path in self.paths:
            try:
                size = self.get_total_size(path)
                sizes[path] = size
            except Exception as e:
                sizes[path] = f'Error: {e}'
        return sizes

    def get_total_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def calculate_confidence_level(self, estimated_size, actual_size):
        if actual_size == 0:
            return "Unknown"
        confidence = (estimated_size / actual_size) * 100
        return self.classify_confidence(confidence)

    def classify_confidence(self, confidence):
        if confidence >= 90:
            return "High"
        elif confidence >= 70:
            return "Medium"
        else:
            return "Low"