def print_table(records, fields, formatter):
#     print(' '.join('%10s' % fieldname for fieldname in fields))
#     print(('-'*10 + ' ')*len(fields))
#     for record in records:
#         print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))
    formatter.headings(fields)
    for r in records:
        rowdata= [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)      
        
class TableFormatter:       #An Abstract Base Class (ABC)
    def headings(self, headers):
        raise NotImplementedError()

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

def create_formatter(fmt):
    if fmt == 'text':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise NotImplementedError

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