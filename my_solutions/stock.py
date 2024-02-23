from structure import Structure
from validate import String, PositiveFloat, PositiveInteger

# @validate_attributes
class Stock(Structure):
    # _fields = ('name', 'shares', 'price')
    # def __init__(self, name, shares, price):
    #     self._init()

    name= String()
    shares= PositiveInteger()
    price= PositiveFloat()
    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

# Stock.set_fields()
# Stock.create_init()