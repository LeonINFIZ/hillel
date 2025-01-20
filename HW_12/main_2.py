class Item:
    """
    Class representing an item in the store.

    Attributes:
        name (str): The name of the item.
        price (float): The price of the item.
        description (str): A brief description of the item.
        dimensions (str): The dimensions or size of the item.
    """

    def __init__(self, name: str, price: float, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: ${self.price}"


class User:
    """
    Class representing a user (customer).

    Attributes:
        name (str): The first name of the user.
        surname (str): The last name of the user.
        numberphone (str): The phone number of the user.
    """

    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Purchase:
    """
    Class representing a purchase order.

    Attributes:
        user (User): The user who made the purchase.
        products (Dict[Item, int]): A dictionary of items and their quantities.
        total (float): The total cost of the order.
    """

    def __init__(self, user: User):
        self.user = user
        self.products: Dict[Item, int] = {}
        self.total: float = 0.0

    def add_item(self, item: Item, cnt: int) -> None:
        """
        Adds an item to the purchase order.

        If the item already exists in the order, its quantity is updated.

        Args:
            item (Item): The item to add.
            cnt (int): The quantity of the item.
        """
        self.total += item.price * cnt

        if item not in self.products:
            self.products[item] = cnt
        else:
            self.products[item] += cnt

    def get_total(self) -> float:
        """
        Returns the total cost of the purchase order.

        Returns:
            float: The total cost of the order.
        """
        return self.total

    def __str__(self) -> str:
        """
        Returns a string representation of the purchase order.

        Includes details about the user, items, and total cost.

        Returns:
            str: A formatted string representation of the order.
        """
        text = (f"User:\n\t{self.user.name} {self.user.surname}, {self.user.numberphone}\n"
                f"Items:\n")

        for item, quantity in self.products.items():
            text += f"\t{item}, x{quantity} = ${item.price * quantity}\n"

        text += f"Total cost:\n\t${self.total:.2f}"
        return text


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5
print(apple, "\n")  # lemon, price: 5

buyer = User("Artem", "Topalov", "88005553535")
print(buyer, "\n")  # Artem Topalov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
cart.add_item(apple, 10)
print(cart)
