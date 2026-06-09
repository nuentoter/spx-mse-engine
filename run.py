from spx.parser import parse
from spx.runtime import Runtime

def main():
    data = parse("game/forest.spx")

    runtime = Runtime(data)

    runtime.render()

if __name__ == "__main__":
    main()
