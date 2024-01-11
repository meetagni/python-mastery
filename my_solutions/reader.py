import csv
def read_csv_as_dicts(filename, coltypes):
    records=[]
    with open(filename) as f:
        rows= csv.reader(f)
        headers= next(rows)
        for row in rows:
            record= {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            records.append(record)
    return records

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
