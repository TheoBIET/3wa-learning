class Product:
    def __init__(self, **args):
        self._name = args['name']
        self._price = args['price']

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def price(self):
        return (self._price + self.calculate_tax())
    
    @price.setter
    def price(self, price):
        self._price = price

    def calculate_tax(self):
        return self._price * self._tax_percentage / 100

    def calculate_price(self, count):
        return self._price + self.calculate_tax() * count

    _tax_percentage = 20

def total_product_price(products):
    return sum(product.price for product in products if isinstance(product, Product))   

apple = Product(name='Apple', price=1.1)

orange = Product(name='Orange', price=1.2)

print(total_product_price([apple, orange, apple, orange, apple, orange, apple, orange]))