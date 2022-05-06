import json
import numpy as np


def import_predictions(filepath):
    data = None
    with open(filepath, "r") as input_file:
        data = json.load(input_file)
    return data


def extract_features(instances):
    combined = np.array([instance["features"] for instance in instances])
    return combined


if __name__ == "__main__":
    pass
