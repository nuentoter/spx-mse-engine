from time import sleep

from spx.parser import parse
from spx.runtime import Runtime


def main():
    data = parse("game/forest.spx")

    runtime = Runtime(data)

    while True:
        runtime.tick()
        sleep(1)


if __name__ == "__main__":
    main()
