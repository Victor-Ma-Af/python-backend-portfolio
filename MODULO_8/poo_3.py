class Produto:
    def __init__(self, name, price, amount):

        self.name = name
        self.price = price
        self.amount = amount
    def add_to_stock(self, quantity):
        if quantity > 0:
            self.amount += quantity
            return self.amount
        else:
            return "the quantity cannot be negative"
    def remove_to_stock(self, quantity):
        if quantity <= self.amount:
            self.amount -= quantity
            return self.amount
    def total_value(self):
        return self.price * self.amount

arroz = Produto("rice", 10, 20)

print(arroz.remove_to_stock(5))

print(arroz.total_value())
        
