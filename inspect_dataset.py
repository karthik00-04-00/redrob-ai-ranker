import json
from pprint import pprint

with open(
    "data/raw/candidate_schema.json",
    "r",
    encoding="utf-8"
) as f:
    schema = json.load(f)

pprint(schema)