class Item:
    def __init__(self, name,price,quantity):
        print(f"Nombre: {name}",f"Precio: {price} Cantidad: {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 5000, 3)

print(item1.calculate_total_price(), item2.calculate_total_price())
