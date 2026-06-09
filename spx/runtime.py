import time

def move_toward(a, b):
    if a["x"] < b["x"]:
        a["x"] += 1
    elif a["x"] > b["x"]:
        a["x"] -= 1

    if a["y"] < b["y"]:
        a["y"] += 1
    elif a["y"] > b["y"]:
        a["y"] -= 1


def execute_action(action, world, entity_name):
    entity = world[entity_name]

    if action == "print state":
        print(f"[STATE] {entity_name}: {entity}")

    elif action.startswith("chase"):
        _, target_name = action.split(" ", 1)
        target = world.get(target_name)

        if target:
            move_toward(entity, target)


def tick(world):
    print("\n--- TICK ---")

    for name, entity in world.items():
        behavior = entity.get("behavior", [])

        if isinstance(behavior, str):
            behavior = [behavior]

        for action in behavior:
            execute_action(action, world, name)

    for name, data in world.items():
        print(f"{name}: {data}")
