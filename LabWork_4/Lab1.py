import json

FILENAME = "input.json"

def task() -> float:
    final_value = 0

    with open(FILENAME) as f:
        json_data = json.load(f)

    final_value = sum(item["score"] * item["weight"] for item in json_data)

    return round(final_value, 3)

print(task())
