class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_plant(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}:")
        print(f"  {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def get_info(self):
        super().get_info()
        print(f"  Color: {self.color}")
        if self.bloomed:
            print(f"  {self.name} is blooming beautifully!")
        else:
            print(f"  {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.fruiting = False

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide"
        )

    def get_info(self):
        super().get_info()
        print(f"  Trunk Diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        self.height += 2
        self.nutritional_value += 1

    def age_plant(self):
        self.age += 1

    def get_info(self):
        super().get_info()
        print(f"  Harvest Season: {self.harvest_season}")
        print(f"  Nutritional Value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    # Flower example
    print("=== Flower ===")
    rose = Flower("Rose", 15, 10, "red")
    rose.get_info()
    print("\n[asking the rose to bloom]")
    rose.bloom()
    rose.get_info()

    # Tree example
    print("\n=== Tree ===")
    oak = Tree("Oak", 200, 365, 5)
    oak.get_info()
    print("\n[asking the oak to produce shade]")
    oak.produce_shade()

    # Vegetable example
    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.get_info()
    print("\n[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_plant()
    tomato.get_info()
