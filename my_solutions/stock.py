from structly import *
#from validate import String, PositiveFloat, PositiveInteger

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

if __name__ == '__main__':
    # from structly import read_csv_as_instances
    # from structly import create_formatter, print_table
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)