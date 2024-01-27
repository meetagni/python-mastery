import csv
import logging
log= logging.getLogger(__name__)
# def read_csv_as_dicts(filename, coltypes):
#     '''
#     Read CSV data into a list of dictionaries with optional type conversion
#     '''
#     records=[]
#     with open(filename) as f:
#         rows= csv.reader(f)
#         headers= next(rows)
#         for row in rows:
#             record= {name: func(val) for name, func, val in zip(headers, coltypes, row)}
#             records.append(record)
#     return records
# #     parser= DictCSVParser(coltypes)
# #     return parser.parse(filename)

# # class DataCollection:
# #     def __init__(self, *columns):
# #         self.columns = columns
# #         self.data = [[] for _ in range(len(columns))]

# #     def __len__(self):
# #         return len(self.data[0])

# #     def __getitem__(self, index):
# #         return {col: self.data[i][index] for i, col in enumerate(self.columns)}

# # def read_csv_as_columns(filename, types):
# #     with open(filename) as f:
# #         rows = csv.reader(f)
# #         headers = next(rows)
# #         indexes = [headers.index(col) for col in headers]
# #         data = DataCollection(*headers)
# #         for row in rows:
# #             for i, value in zip(indexes, row):
# #                 data.data[i].append(row[i])
# #         return data

# def read_csv_as_instances(filname, cls):
#     '''
#     Read CSV data into a list of instances
#     '''
#     records= []
#     with open(filname) as f:
#         rows= csv.reader(f)
#         headers= next(rows)
#         for row in rows:
#             records.append(cls.from_row(row))
#     return records
#     # parser= InstanceCSVParser(cls)
#     # return parser.parse(filname)
    
# class Row:
#          def __init__(self, route, date, daytype, numrides):
#              self.route = route
#              self.date = date
#              self.daytype = daytype
#              self.numrides = numrides
#          @classmethod
#          def from_row(cls, row):
#              return cls(row[0], row[1], row[2], int(row[3]))

# import csv
# from abc import ABC, abstractmethod
# class CSVParser(ABC):
#     def parse(self, filename):
#         records= []
#         with open(filename) as f:
#             rows= csv.reader(f)
#             headers= next(rows)
#             for row in rows:
#                 record= self.make_record(headers, row)
#                 records.append(record)
#         return records
    
#     @abstractmethod
#     def make_record(self, headers, row):
#         pass

# class DictCSVParser(CSVParser):
#     def __init__(self, types):
#         self.types= types
#     def make_record(self, headers, row):
#         return {name: func(val) for name, func, val in zip(headers, self.types, row)}

# class InstanceCSVParser(CSVParser):
#     def __init__(self, cls):
#         self.cls= cls
#     def make_record(self, headers, row):
#         return self.cls.from_row(row)

from typing import List

def csv_as_dicts(lines, types, *, headers=None):
    '''Read lines from an interable object into dictionaries.'''
    # records = []
    # rows = csv.reader(lines)
    # if headers is None:
    #     headers = next(rows)
    # for row in rows:
    #     record = { name: func(val)
    #                for name, func, val in zip(headers, types, row) }
    #     records.append(record)
    # return records
    return convert_csv(lines, lambda headers, row: {name: func(val) for name, func, val in zip(headers, types, row)})
def csv_as_instances(lines, cls, *, headers=None):
    '''Read lines into instances.'''
    # records = []
    # rows = csv.reader(lines)
    # if headers is None:
    #     headers = next(rows)
    # for row in rows:
    #     record = cls.from_row(row)
    #     records.append(record)
    # return records
    return convert_csv(lines, lambda headers, row: cls.from_row(row))

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)
def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
    
def convert_csv(lines, func, *, headers=None):
    '''Unified convert csv to dict or instance'''
    records= []
    rows= csv.reader(lines)
    if headers is None:
        headers= next(rows)
    # # for row in rows:
    # #     record= func(headers, row)
    # #     records.append(record)
    # # return records
    # return map(lambda row: func(headers, row), rows)
    for rowno, row in enumerate(rows, start=1):
        try:
            records.append(func(headers, row))
        except ValueError as e:
            log.warning('Row %s: Bad row: %s', rowno, row)
            log.debug('Row %s: Reason: %s', rowno, row)
    return records