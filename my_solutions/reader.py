import csv
def read_csv_as_dicts(filename, coltypes):
    # records=[]
    # with open(filename) as f:
    #     rows= csv.reader(f)
    #     headers= next(rows)
    #     for row in rows:
    #         record= {name: func(val) for name, func, val in zip(headers, coltypes, row)}
    #         records.append(record)
    # return records
    parser= DictCSVParser(coltypes)
    return parser.parse(filename)

class DataCollection:
    def __init__(self, *columns):
        self.columns = columns
        self.data = [[] for _ in range(len(columns))]

    def __len__(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return {col: self.data[i][index] for i, col in enumerate(self.columns)}

def read_csv_as_columns(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        indexes = [headers.index(col) for col in headers]
        data = DataCollection(*headers)
        for row in rows:
            for i, value in zip(indexes, row):
                data.data[i].append(row[i])
        return data

def read_csv_as_instances(filname, cls):
    # records= []
    # with open(filname) as f:
    #     rows= csv.reader(f)
    #     headers= next(rows)
    #     for row in rows:
    #         records.append(cls.from_row(row))
    # return records
    parser= InstanceCSVParser(cls)
    return parser.parse(filname)
    
class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

import csv
from abc import ABC, abstractmethod
class CSVParser(ABC):
    def parse(self, filename):
        records= []
        with open(filename) as f:
            rows= csv.reader(f)
            headers= next(rows)
            for row in rows:
                record= self.make_record(headers, row)
                records.append(record)
        return records
    
    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types= types
    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls= cls
    def make_record(self, headers, row):
        return self.cls.from_row(row)