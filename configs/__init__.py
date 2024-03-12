import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
params_path = os.path.join(dir_path, 'params.yaml')
def get_conf():
    with open(params_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


config = get_conf()
