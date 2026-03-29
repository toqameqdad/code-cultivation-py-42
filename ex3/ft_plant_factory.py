class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def create_garden():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    return plants


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden = create_garden()

    for plant in garden:
        print("Created:", end=" ")
        plant.get_info()
