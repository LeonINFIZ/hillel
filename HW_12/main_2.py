class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: ${self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:

    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.total += item.price * cnt

        if item not in self.products:
            self.products[item] = cnt
        else:
            self.products[item] += cnt

    def __str__(self):
        text = (f"User:\n\t{self.user.name} {self.user.surname}, {self.user.numberphone}\n"
                f"Items:\n")

        for key, value in self.products.items():
            text += f"\t{key}, x{value} = ${key.price * value}\n"

        text += "Total cost:\n\t$" + str(self.total)
        return text

    def get_total(self):
        return self.total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon, "\n")  # lemon, price: 5

buyer = User("Artem", "Topalov", "88005553535")
print(buyer, "\n")  # Artem Topalov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
cart.add_item(apple,
              10)  # Ранее в коде из задания была недоработка, item перезаписывался, а не добавлялся как следовало бы логике add

print(cart)
