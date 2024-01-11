import csv
import collections

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
    records= RideData()
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

#As columns
def read_rides_as_columns(filename):
    '''
    read the bus ride data as into 4 lists, representing columns
    '''
    routes=[]
    dates=[]
    daytypes=[]
    numrides=[]
    with open(filename) as f:
        rows= csv.reader(f)
        headings= next(f)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes=[]
        self.dates=[]
        self.daytypes=[]
        self.numrides=[]
    def __len__(self):
        return len(self.routes) #assuming all lists have the same length
    def __getitem__(self, index):
        return {
            'route': self.routes[index],
            'date': self.dates[index],
            'daytype': self.daytypes[index],
            'rides': self.numrides[index]
        }    
    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
        
        
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.routes))
            return [dict(routes= self.routes[i], dates= self.dates[i], daytypes= self.daytypes[i], numrides= self.numrides[i]) for i in range(start, stop, step)]
        elif isinstance(index, int):
            return dict(routes= self.routes[index], dates= self.dates[index], daytypes= self.daytypes[index], numrides= self.numrides[index])
        else:
            raise TypeError("Invalid argument type.")