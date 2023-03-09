
import os
import yaml
from pprint import pprint

HERE = os.path.dirname(os.path.abspath(__file__))
print(HERE)

def load_blueprint(name):
    with open(os.path.join(HERE, "blueprints", name, "resources.yml")) as f:
        return yaml.safe_load(f.read())


def test_hello_world():
    print(HERE)
    blueprint = load_blueprint('hello_world')
    pprint(blueprint)
    assert blueprint['resources'][0]['hello_world']['message'] == 'Hello World!'
