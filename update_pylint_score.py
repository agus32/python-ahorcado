import json
import os

score = os.getenv('score')

data = {
    "schemaVersion": 1,
    "label": "Pylint Score",
    "message": f"{score}/10",
    "color": "blue" if float(score) >= 8 else "red"
}

with open("pylint_score.json", "w") as f:
    json.dump(data, f)
