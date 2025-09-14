import json

data = {
    "name": "Muhammad Usman Amjad",
    "tutorials_created": 5,
    "status": "success"
}

# Save to results.json
with open("results.json", "w") as f:
    json.dump(data, f, indent=4)

print("results.json created!")
