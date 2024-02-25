__all__=['print_table', 'create_formatter']

def print_table(records, fields, formatter):
#     print(' '.join('%10s' % fieldname for fieldname in fields))
#     print(('-'*10 + ' ')*len(fields))
#     for record in records:
#         print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata= [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)      
        
from abc import ABC, abstractmethod
class TableFormatter(ABC):       #An Abstract Base Class (ABC)
    _formats={}
    
    @classmethod
    def __init_subclass__(cls):
        name= cls.__module__.split('.')[-1]
        TableFormatter._formats[name]= cls
    
    @abstractmethod
    def headings(self, headers):
        pass
    @abstractmethod
    def row(self, rowdata):
        pass

# from .formats.text import TextTableFormatter
# from .formats.csv import CSVTableFormatter
# from .formats.html import HTMLTableFormatter

def create_formatter(fmt, column_formats=None, upper_headers=False):
    # if fmt == 'text':
    #     formatter_cls= TextTableFormatter
    # elif fmt == 'csv':
    #     formatter_cls= CSVTableFormatter
    # elif fmt == 'html':
    #     formatter_cls= HTMLTableFormatter
    # else:
    #     raise RuntimeError("Unknown format %s" % fmt)
    
    if fmt not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{fmt}')
    
    formatter_cls= TableFormatter._formats.get(fmt)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % fmt)
    
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats= column_formats
    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass
    return formatter_cls()

# import sys
# class redirect_stdout:
#     def __init__(self, out_file):
#             self.out_file = out_file
#     def __enter__(self):
#         self.stdout = sys.stdout
#         sys.stdout = self.out_file
#         return self.out_file
#     def __exit__(self, ty, val, tb):
#         sys.stdout = self.stdout

class ColumnFormatMixin:
    formats= []
    def row(self, rowdata):
        rowdata= [(fmt %d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])