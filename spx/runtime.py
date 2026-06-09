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


def apply_behavior(name, world):
    entity = world[name]

    if "behavior" not in entity:
        return

    behavior = entity["behavior"]

    if behavior == "chase_player":
        player = world.get("player")
        if player:
            move_toward(entity, player)


def tick(world):
    print("\n--- TICK ---")

    # run behaviors
    for name in world.keys():
        apply_behavior(name, world)

    # print world state
    for name, data in world.items():
        print(f"{name}: {data}")
