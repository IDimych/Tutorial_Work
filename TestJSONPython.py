import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
print(data)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)