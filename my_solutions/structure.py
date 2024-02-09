import sys
import inspect
class Structure:
    _fields= ()
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