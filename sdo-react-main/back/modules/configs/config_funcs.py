import os
import json


def load_config():
    # Путь к config.json на две директории выше
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')
    with open(config_path, 'r') as file:
        config_data = json.load(file)
    return config_data

