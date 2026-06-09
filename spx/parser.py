import re

ENTITY_HEADER = "⬢"

def parse_list(value):
    value = value.strip()

    if not (value.startswith("[") and value.endswith("]")):
        return value

    inner = value[1:-1].strip()

    if not inner:
        return []

    items = [i.strip() for i in inner.split(",")]
    return items


def parse_spx(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entities = {}
    current = None

    for line in lines:
        line = line.strip()

        if line.startswith(ENTITY_HEADER):
            name = line.replace(ENTITY_HEADER, "").replace("{", "").strip()
            current = name
            entities[current] = {}
            continue

        if line == "}":
            current = None
            continue

        if current and "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            # list support
            value = parse_list(value)

            # int conversion
            if isinstance(value, str) and re.match(r"^-?\d+$", value):
                value = int(value)

            entities[current][key] = value

    return entities
