import os
import yaml
import json
from jsonschema import validate

HERE = os.path.dirname(os.path.abspath(__file__))


def load_blueprint(name):
    with open(os.path.join(HERE, "blueprints", name, "resources.yml")) as f:
        return yaml.safe_load(f.read())


def load_schema(name):
    with open(
        os.path.join(HERE, "blueprints", name, "resource_schema.json")
    ) as f:
        return json.loads(f.read())


def validate_blueprint(name):
    blueprint = load_blueprint(name)
    blueprint_schema = load_schema(name)
    validate(blueprint, blueprint_schema)


def test_hello_world():
    blueprint = load_blueprint("hello_world")
    assert (
        blueprint["resources"][0]["hello_world"]["message"] == "Hello World!"
    )
    assert validate_blueprint("hello_world") is None
