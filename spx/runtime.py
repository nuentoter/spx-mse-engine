class Runtime:
    def __init__(self, data):
        self.entities = data["entities"]

    def render(self):
        print("\n=== WORLD STATE ===")

        for name, values in self.entities.items():
            print(name)

            for k, v in values.items():
                print(f"  {k}: {v}")
