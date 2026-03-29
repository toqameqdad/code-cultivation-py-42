class Plant:
    def __init__(self, name, height, age, daily_growth):
        self.name = name
        self.height = height
        self.age = age
        self.daily_growth = daily_growth

    def grow(self):
        self.height += self.daily_growth

    def age_plant(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30, 0.8)
    start_height = rose.height

    print("=== Garden Plant Growth ===")

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.get_info()
        rose.grow()
        rose.age_plant()

    growth_week = rose.height - start_height
    print(f"Growth this week: {round(growth_week)}cm")
