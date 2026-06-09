import time

def move_toward(a, b):
    """
    Move point a one step toward point b
    """
    if a["x"] < b["x"]:
        a["x"] += 1
    elif a["x"] > b["x"]:
        a["x"] -= 1

    if a["y"] < b["y"]:
        a["y"] += 1
    elif a["y"] > b["y"]:
        a["y"] -= 1


def tick(world):
    print("\n--- TICK ---")

    player = world.get("player")
    wolf = world.get("wolf")

    # behavior: wolf chases player
    if player and wolf:
        move_toward(wolf, player)

    # print updated world
    for name, data in world.items():
        print(f"{name}: {data}")
