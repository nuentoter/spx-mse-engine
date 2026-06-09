class Runtime:
    def __init__(self, data):
        self.entities = data["entities"]
        self.tick_count = 0

    def tick(self):
        self.tick_count += 1

        print(f"\n=== TICK {self.tick_count} ===")

        self.update_world()
        self.render()

    def update_world(self):
        player = self.entities.get("player")
    wolf = self.entities.get("wolf")

    if not player or not wolf:
        return

    if wolf["x"] > player["x"]:
        wolf["x"] -= 1
    elif wolf["x"] < player["x"]:
        wolf["x"] += 1

    if wolf["y"] > player["y"]:
        wolf["y"] -= 1
    elif wolf["y"] < player["y"]:
        wolf["y"] += 1

    def render(self):
        for name, values in self.entities.items():
            print(name)

            for k, v in values.items():
                print(f"  {k}: {v}")
