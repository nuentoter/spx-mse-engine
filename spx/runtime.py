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


def distance(a, b):
    return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])


def evaluate_condition(condition, world, entity_name):
    entity = world[entity_name]

    if condition.startswith("near"):
        _, target_name = condition.split(" ", 1)
        target = world.get(target_name)
        if not target:
            return False

        return distance(entity, target) <= 2

    return False


def execute_action(action, world, entity_name):
    entity = world[entity_name]

    if action == "chase player":
        move_toward(entity, world["player"])

    elif action == "wander":
        # minimal random-ish drift (deterministic for now)
        entity["x"] += 1


def run_behavior(behavior, world, entity_name):
    for rule in behavior:
        if "->" in rule:
            condition, action = rule.split("->")
            condition = condition.strip()
            action = action.strip()

            if evaluate_condition(condition, world, entity_name):
                execute_action(action, world, entity_name)
                return  # stop after first matched rule
        else:
            execute_action(rule, world, entity_name)


def tick(world):
    print("\n--- TICK ---")

    for name, entity in world.items():
        behavior = entity.get("behavior", [])

        if isinstance(behavior, str):
            behavior = [behavior]

        run_behavior(behavior, world, name)

    for name, data in world.items():
        print(f"{name}: {data}")
