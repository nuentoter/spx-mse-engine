from spx.parser import parse_spx
from spx.runtime import tick
import time

if __name__ == "__main__":
    world = parse_spx("game/forest.spx")

    while True:
        tick(world)
        time.sleep(1)
