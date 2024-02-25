from validate import Validator, validated
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)
    
    @staticmethod
    def __new__(meta, name, bases, methods):
        methods= methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
    _fields= ()
    _types= ()
    # def __init__(self, *args):
    #     if len(args) != len(self._fields):
    #         raise TypeError(f'Expected {len(self._fields)} arguments')
    #     for name, arg in zip(self._fields, args):
    #         setattr(self, name, arg)
    # @staticmethod
    # def _init():
    #     locs= sys._getframe(1).f_locals
    #     self= locs.pop('self')
    #     for name, val in locs.items():
    #         setattr(self, name, val)
    
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join(repr(getattr(self, name)) for name in self._fields))
    
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
    
    # @classmethod
    # def set_fields(cls):
    #     sig= inspect.signature(cls)
    #     cls._fields= tuple(sig.parameters)
    
    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        code = 'def __init__(self, {0}):\n'.format(args)
        statements = [ '    self.{0} = {0}'.format(name) for name in cls._fields]
        code += '\n'.join(statements)
        locs = { }
        exec(code, locs)
        cls.__init__ = locs['__init__']
    
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
    
    @classmethod
    def from_row(cls, row):
        rowdata= [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)
    
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
    
    def __eq__(self,other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)

def validate_attributes(cls):
    validators=[]
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))
        
    cls._fields= tuple([val.name for val in validators])
    cls._types= tuple([getattr(v, 'expected_type', lambda x: x) for v in validators])
    if cls._fields:    
        cls.create_init()
    
    return cls

def typed_structure(clsname, **validators):
    cls= type(clsname, (Structure,), validators)
    return cls