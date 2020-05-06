import yaml


def parse_yaml(name):
    return yaml.safe_load(open(name))
