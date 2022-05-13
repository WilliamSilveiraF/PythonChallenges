class Property:
    def __init__(self, address, price):
        self.address = address
        self.price = price

class New(Property):
    pass
    def __init__(self, address, price, additionalPrice):
        Property.__init__(self, address, price)
        self.additionalPrice = additionalPrice

    def getAdditionalPrice(self):
        return self.additionalPrice

    def getPrice(self):
        return self.additionalPrice + self.price

class Old(Property):
    pass
    def __init__(self, address, price):
        Property.__init__(self, address, price)
        self.discount = 0.15 * price

    def getDiscount(self):
        return self.discount

    def getPrice(self):
        return self.price - self.discount
teste = Old('Rua carlos', 100000)

print(teste.getDiscount())


