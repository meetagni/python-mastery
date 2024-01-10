import csv

#A list of tuples
def read_rides_as_tuples(filename):
    '''
    read the bus ride data as a list of tuples
    '''
    records=[]
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record=(route, date, daytype, rides)
            records.append(record)
    return records

#A dictionary
def read_rides_as_dictionary(filename):
    '''
    read the bus ride data as a list of dictionaries
    '''
    records=[]
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record = {
                    'route': route,
                    'date': date,
                    'daytype': daytype,
                    'rides': rides,
                    }
            records.append(record)
    return records

#A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class(filename):
    '''
    read the bus ride data as a list of class objects
    '''
    records=[]
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record=Row(route, date, daytype, rides)
            records.append(record)
    return records

#Named tuple
import typing
class Rides_namedtuple(typing.NamedTuple):
    route : str
    date : str
    daytype : str
    rides : int
def read_rides_as_namedtuple(filename):
    '''
    read the bus ride data as a list of namedtuples
    '''
    records= []
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record= Rides_namedtuple(route, date, daytype, rides)
            records.append(record)
    return records

#A class with slots
class Row_with_slots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
        
def read_rides_as_class_with_slots(filename):
    '''
    read the bus ride data as a list of class objects
    '''
    records=[]
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record=Row_with_slots(route, date, daytype, rides)
            records.append(record)
    return records

#Dataclass
from dataclasses import dataclass
@dataclass
class Row_dataclass:
    route : str
    date : str
    daytype : str
    rides : int
def read_rides_as_dataclass(filename):
    '''
    read the bus ride data as dataclass
    '''
    records= []
    with open(filename) as f:
        rows=csv.reader(f)
        headings=next(rows)
        for row in rows:
            route=row[0]
            date=row[1]
            daytype=row[2]
            rides=int(row[3])
            record= Row_dataclass(route, date, daytype, rides)
            records.append(record)
    return records