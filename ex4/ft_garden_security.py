class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = float(height)
        self._age = age

    def get_info(self):
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can’t be negative")
            print("Height update rejected")
            return
        self._height = value
        print(f"Height updated: {self._height}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = value
        print(f"Age updated: {self._age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    print(f"Plant created: {rose.get_info()}\n")

    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-5)
    rose.set_age(-10)

    print(f"\nCurrent state: {rose.get_info()}")
