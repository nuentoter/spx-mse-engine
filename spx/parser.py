import re

ENTITY_HEADER = "⬢"

def parse_spx(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entities = {}
    current = None

    for line in lines:
        line = line.strip()

        # detect entity start
        if line.startswith(ENTITY_HEADER):
            name = line.replace(ENTITY_HEADER, "").strip().replace("{", "").strip()
            current = name
            entities[current] = {}
            continue

        # detect end block
        if line == "}":
            current = None
            continue

        # parse key = value
        if current and "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            # only integer parsing for now
            if re.match(r"^-?\d+$", value):
                value = int(value)

            entities[current][key] = value

    return entities
