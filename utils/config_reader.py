import os
import yaml

def read_config():
    # Gets absolute path regardless of working directory
    base_path = os.path.dirname(os.path.dirname(__file__))  # go up from utils/ to root
    config_path = os.path.join(base_path, "config", "config.yaml")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
