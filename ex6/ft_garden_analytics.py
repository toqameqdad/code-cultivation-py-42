class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, {self.show_calls} show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = Plant._Stats()

    def grow(self):
        self.height += 1
        self.stats.grow_calls += 1

    def age_plant(self, days=1):
        self.age += days
        self.stats.age_calls += 1

    def get_info(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats.show_calls += 1

    def display_stats(self):
        self.stats.display()

    def show_statistics(self):
        print(f"[statistics for {self.name}]")
        self.display_stats()

    @staticmethod
    def is_older_than_years(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def grow(self):
        super().grow()
        self.height += 7

    def get_info(self):
        super().get_info()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._shade_calls = 0

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )
        self._shade_calls += 1

    def get_info(self):
        super().get_info()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self):
        super().display_stats()
        print(f"{self._shade_calls} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def grow(self):
        super().grow()
        self.height += 22

    def get_info(self):
        super().get_info()
        print(f"Seeds: {self.seeds}")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_years(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_years(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.get_info()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.get_info()
    rose.show_statistics()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.get_info()
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_statistics()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.get_info()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_plant(20)  # تحديث العمر مرة واحدة لتوافق المثال
    sunflower.bloom()
    sunflower.get_info()
    sunflower.show_statistics()

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.get_info()
    unknown.show_statistics()
