#readport.py
import csv

#a function that reads a fileinrto a list of dicts
def read_portfolio(filename):
    portfolio= []
    with open(filename) as f:
        rows= csv.reader(f)
        header= next(rows)
        for row in rows:
            record={
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio