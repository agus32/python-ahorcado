import json
import os

score = os.getenv('score')
print(score)

data = {
    "schemaVersion": 1,
    "label": "Pylint Score",
    "message": f"{score}",
    "color": "blue" if (score) >= "8" else "red"
}

with open("pylint_score.json", "w") as f:
    json.dump(data, f)
