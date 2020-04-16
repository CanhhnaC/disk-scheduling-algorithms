import json
import sys

def load(name):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data[name]
    except Exception:
        pass


def save(name, value, distance, sequence):
    with open('data.json', 'w') as f:
        x = {
            name: value,
            distance: sequence
        }
        json.dump(x, f)
