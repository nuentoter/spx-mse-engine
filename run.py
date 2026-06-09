from spx.parser import parse_spx

if __name__ == "__main__":
    world = parse_spx("game/forest.spx")
    print(world)
