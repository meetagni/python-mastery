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
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10+' ')*len(headers))
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>%s</th>' % h, end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>%s</td>' % d, end=' ')
        print('</tr>')

def create_formatter(fmt, column_formats=None, upper_headers=False):
    if fmt == 'text':
        formatter_cls= TextTableFormatter
    elif fmt == 'csv':
        formatter_cls= CSVTableFormatter
    elif fmt == 'html':
        formatter_cls= HTMLTableFormatter
    else:
        raise RuntimeError("Unknown format %s" % fmt)
    
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats= column_formats
    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass
    return formatter_cls()

import sys
class redirect_stdout:
    def __init__(self, out_file):
            self.out_file = out_file
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file
    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout

class ColumnFormatMixin:
    formats= []
    def row(self, rowdata):
        rowdata= [(fmt %d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])