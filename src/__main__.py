import json

from planqk.commons.json import any_to_json
from planqk.commons.logging import init_logging

from .program import InputParams, run, InputData

init_logging()

# This file is executed if you run `python -m src` from the project root. Use this file to test your program locally.
# You can read the input data from the `input` directory and map it to the respective parameter of the `run()` function.

with open(f"./input/data.json") as file:
    data = InputData.model_validate(json.load(file))

with open(f"./input/params.json") as file:
    params = InputParams.model_validate(json.load(file))

result = run(data, params)

print(any_to_json(result))
