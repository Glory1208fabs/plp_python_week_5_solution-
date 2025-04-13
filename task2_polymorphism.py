class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def move(self):
        print("The dog runs on four legs 🐕")


class Bird(Animal):
    def move(self):
        print("The bird flies in the sky 🐦")


class Fish(Animal):
    def move(self):
        print("The fish swims in the water 🐟")


# Example usage
if __name__ == "__main__":
    animals = [Dog(), Bird(), Fish()]

    for animal in animals:
        animal.move()