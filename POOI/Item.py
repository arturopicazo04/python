class Item:
    pay_rate = 0.8  # The pay rate after 20% discaunt
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        print(f"Nombre: {name}", f"Precio: {price} Cantidad: {quantity}")
        # Run validations to the received argument
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 5000, 3)
item3 = Item("Headphones", 200, 4)
item4 = Item("Keyboard", 150, 6)
item5 = Item("Monitor", 600, 8)

print(Item.all)

# for instance in Item.all:
#     print(instance.name)
#
# item1.apply_discount()
# print(item1.price)
#
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)

# print (Item.__dict__)   # All the attributes for Class level
# print (item1.__dict__) # All the attributes for instance level


# print(item1.calculate_total_price(), item2.calculate_total_price())
