class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_info(self):
        print(f"{self.name}:")
        print(f"  {self._height:.1f}cm, {self._age} days old")

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height cannot be negative")
            print("Height update rejected")
        else:
            self._height = value
            print("Height updated:")
            print(f"{self._height}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print("Age updated:")
            print(f"{self._age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":

    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)

    print("Plant created:\n")
    rose.get_info()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print("\nCurrent state:")
    rose.get_info()
