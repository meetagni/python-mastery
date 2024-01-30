# class Stock:
#     __slots__= ('name', '_shares', '_price')
#     _types= (str, int, float)
    
#     def __init__(self, name, shares, price):
#         self.name= name
#         self.shares= shares
#         self.price= price
    
#     @property
#     def cost(self):
#         return self.shares * self.price
    
#     @property
#     def shares(self):
#         return self._shares
#     @shares.setter
#     def shares(self, value):
#         if not isinstance(value, self._types[1]) or value<0:
#             raise TypeError("Shares must be a positive integer")
#         self._shares=value
    
#     @property
#     def price(self):
#         return self._price
#     @price.setter
#     def price(self, value):
#         if not isinstance(value, self._types[2]) or value<0.0:
#             raise TypeError("Price must be a positive float")
#         self._price= value
    
#     def sell(self, nshares):
#         self.shares-=nshares
        
#     @classmethod
#     def from_row(cls, row):
#         values= [func(val) for func, val in zip(cls._types, row)]
#         return cls(*values)
    
#     def __repr__(self):
#         return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'
#         # return 'Stock(%s, %d, %.2f)' % (self.name, self._shares, self._price)
    
#     def __eq__(self, other):
#         return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price))
        
# # def read_portfolio(filename):
# #     import csv
# #     portfolio =[]
# #     with open(filename) as f:
# #         rows= csv.reader(f)
# #         headers=next(rows)
# #         for row in rows:
# #             #s= Stock(row[0], int(row[1]), float(row[2]))
# #             s= DStock.from_row(row)
# #             portfolio.append(s)
# #     return portfolio

# def print_portfolio(portfolio):
#     print('%10s %10s %10s' % ('name', 'shares', 'price'))
#     print(('-'*10+' ')*3)
#     for s in portfolio:
#         print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

# from decimal import Decimal
# from typing import Any
# class DStock(Stock):
#     types= (str, int, Decimal)

# import reader
# if __name__ == '__main__':
#     portfolio = reader.read_csv_as_instances('Data/portfolio.csv', Stock)
#     print_portfolio(portfolio)

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
    
    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'