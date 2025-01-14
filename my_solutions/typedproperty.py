def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value

def String(name):
    return typedproperty(name, str)
def Integer(shares):
    return typedproperty(shares, int)
def Float(price):
    return typedproperty(price, float)