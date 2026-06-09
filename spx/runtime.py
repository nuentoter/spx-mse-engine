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
        pass

    def render(self):
        for name, values in self.entities.items():
            print(name)

            for k, v in values.items():
                print(f"  {k}: {v}")
