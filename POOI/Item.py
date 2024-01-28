import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discaunt
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # print(f"Nombre: {name}", f"Precio: {price} Cantidad: {quantity}")
        # Run validations to the received argument
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)

    @property
    # ReadOnly
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("It cant be negative")
        else:
            self.__price = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        # Second parameter is to set the permission of reading
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __connect(self,smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello SomeOne.
        We have {self.name} {self.quantity} times.
        Regards,
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    #
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

    # Actions to execute
