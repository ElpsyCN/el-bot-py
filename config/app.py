import os
import yaml
import json


class Config:
    def parse_yaml(self, file):
        return yaml.safe_load(open(file)) or {}

    def print_json(self):
        print(json.dumps(self.data, ensure_ascii=False, sort_keys=True,
                         indent=2, separators=(',', ': ')))

    def merge(self, folder):
        config = {}
        files = os.listdir(folder)
        for file in files:
            config.update(self.parse_yaml(folder + file))
        return config

    def __init__(self, path):
        if os.path.isdir(path):
            self.data = self.merge(path)
        else:
            self.data = self.parse_yaml(path)
