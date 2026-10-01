import json

from pathlib import Path

#names = ["Alice", "Bob", "Charlie", "David", "Eve"]
#
#with Path("names.json").open("w") as file:
#    contents = json.dumps(names)
#    file.write(contents)


with Path("names.json").open("r") as file:
    contents = json.load(file)
    print(contents[0])  # Output: Alice



