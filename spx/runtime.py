import time

def tick(world):
    """
    Minimal simulation tick:
    For now we just print state evolution placeholder.
    Later this becomes movement, combat, AI, etc.
    """
    print("\n--- TICK ---")
    for name, data in world.items():
        print(f"{name}: {data}")
