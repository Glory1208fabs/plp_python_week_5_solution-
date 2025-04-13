class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive!")

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} (${self.__price})"


    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive!")

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} (${self.__price})"



class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition, GPU: {self.gpu}, Price: ${self.get_price()})"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    print(phone)
    phone.call("123-456-7890")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1299, "Adreno 730")
    print(gaming_phone)
    gaming_phone.play_game("Genshin Impact")
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition, GPU: {self.gpu}, Price: ${self.get_price()})"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    print(phone)
    phone.call("123-456-7890")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 1299, "Adreno 730")
    print(gaming_phone)
    gaming_phone.play_game("Genshin Impact")