#Chapter 5: Date and Time

#Parsing a string into a timezone aware datetime object
# import datetime
# dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
# print(dt)

#Constructing timezone-aware datetimes
# from datetime import datetime, timedelta, timezone 
# JST = timezone(timedelta(hours=+9))
# dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST) 
# print(dt)
# print(dt.tzname()) 
# dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST')) 
# print(dt.tzname())

#Computing time differences
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# then = datetime(2016, 5, 23)
# print(then)
# delta = now-then
# print(delta)
# print(delta.days)
# print(delta.seconds)
#n day's after date:
# def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
#     date_n_days_after = datetime.now() + timedelta(days=add_days) 
#     return date_n_days_after.strftime(date_format)

# a = get_n_days_after_date()
# print(a)
# #n day's before date:
# def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
#     date_n_days_after = datetime.now() - timedelta(days=add_days) 
#     return date_n_days_after.strftime(date_format)

# a = get_n_days_after_date()
# print(a)

#Basic datetime objects usage
# import datetime
# today = datetime.date.today()
# new_year = datetime.date(2017, 1, 1) 
# noon = datetime.time(12, 0, 0)
# now = datetime.datetime.now()
# millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0) 
# print(today)
# print(new_year)
# print(noon)
# print(now)
# print(millenium_turn)

#Switching between time zones
# from datetime import datetime 
# from dateutil import tz
# utc = tz.tzutc()
# local = tz.tzlocal()
# utc_now = datetime.utcnow() 
# print(utc_now)
# utc_now = utc_now.replace(tzinfo=utc) 
# print(utc_now)
# local_now = utc_now.astimezone(local) 
# print(local_now)

#Simple date arithmetic
# import datetime
# today = datetime.date.today()
# print("Today:",today)
# yesterday = today - datetime.timedelta(days=1)
# print('Yesterday:', yesterday)
# tomorrow = today + datetime.timedelta(days=1)
# print('Tomorrow:', tomorrow)
# print('Time between tomorrow and yesterday:', tomorrow - yesterday)

#Converting timestamp to datetime
# import time
# from datetime import datetime 
# seconds_since_epoch=time.time() 
# print(seconds_since_epoch)
# utc_date=datetime.utcfromtimestamp(seconds_since_epoch)
# print(utc_date)

#Subtracting months from a date accurately
# import calendar
# from datetime import date
# def monthdelta(date, delta):
#     m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12 
#     if not m: m = 12
#     d = min(date.day, calendar.monthrange(y, m)[1])
#     return date.replace(day=d,month=m, year=y)
# next_month = monthdelta(date.today(), 1)
# print(next_month)

#Get an ISO 8601 timestamp
#Without timezone, with microseconds
# from datetime import datetime
# print(datetime.now().isoformat())
# #With timezone, with microseconds
# from datetime import datetime
# from dateutil.tz import tzlocal
# print(datetime.now(tzlocal()).isoformat())
# # Out: '2016-07-31T23:09:43.535074-07:00'
# #With timezone, without microseconds
# from datetime import datetime
# from dateutil.tz import tzlocal
# print(datetime.now(tzlocal()).replace(microsecond=0).isoformat())

#Fuzzy datetime parsing (extracting datetime out of a text)
# from dateutil.parser import parse
# dt = parse( "Today is January 1, 2047 at 8:21:00AM",fuzzy=True)
# print(dt)

# Iterate over dates
# import datetime
# day_delta = datetime.timedelta(days=1)
# print(day_delta)
# start_date = datetime.date.today()
# print(start_date)
# end_date = start_date + 7*day_delta
# print(end_date)
# for i in range((end_date - start_date).days):
#  print(start_date + i*day_delta)

# Chapter 6-Date Formatting

#Time between two date-times
# from datetime import datetime
# a = datetime(2016,10,6,0,0,0)
# b = datetime(2016,10,1,23,59,59)
# print(a-b)
# print((a-b).days)
# print((a-b).total_seconds())

#Outputting datetime object to string
# from datetime import datetime
# datetime_for_string = datetime(2016,10,1,0,0)
# datetime_string_format = '%b %d %Y, %H:%M:%S'
# print(datetime.strftime(datetime_for_string,datetime_string_format))

# Parsing string to datetime object
# from datetime import datetime
# datetime_string = 'Oct 1 2016, 00:00:00'
# datetime_string_format = '%b %d %Y, %H:%M:%S'
# print(datetime.strptime(datetime_string, datetime_string_format))

# Chapter 7: Enum

# Creating an enum
# from enum import Enum
# class Color(Enum):
#  red = 1
#  green = 2
#  blue = 3
# print(Color.red) 
# print(Color(1)) 
# print(Color['red']) 

# # Iteration
# class Color(Enum):
#  red = 1
#  green = 2
#  blue = 3
# print([c for c in Color] )

#Chapter 8: Set

# Operations on sets
# Intersection 
# print({1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}))
# print({1, 2, 3, 4, 5} & {3, 4, 5, 6})
# # Union
# print({1, 2, 3, 4, 5}.union({3, 4, 5, 6}))
# print({1, 2, 3, 4, 5} | {3, 4, 5, 6})
# # Difference
# print({1, 2, 3, 4}.difference({2, 3, 5}))
# print({1, 2, 3, 4} - {2, 3, 5})
# # Symmetric difference with
# print({1, 2, 3, 4}.symmetric_difference({2, 3, 5}))
# print({1, 2, 3, 4} ^ {2, 3, 5})
# # Superset check
# print({1, 2}.issuperset({1, 2, 3}))
# print({1, 2} >= {1, 2, 3})
# # Subset check
# print({1, 2}.issubset({1, 2, 3}))
# print({1, 2} <= {1, 2, 3})
# # Disjoint check
# print({1, 2}.isdisjoint({3, 4}))
# print({1, 2}.isdisjoint({1, 4}))

#with single elements
# print(2 in {1,2,3})
# print(4 in {1,2,3})
# print(4 not in {1,2,3})
# # Add and Remove
# s = {1,2,3}
# s.add(4)
# print(s)
# s.discard(3)
# print(s)
# s.discard(5)
# print(s)
# s.remove(2)
# print(s)

#Get the unique elements of a list
# restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
# unique_restaurants = set(restaurants)
# print(unique_restaurants)

#Set of Sets
# print({frozenset({1, 2}), frozenset({3, 4})})

#Set Operations using Methods and Builtins
# a = {1, 2, 2, 3, 4}
# b = {3, 3, 4, 4, 5}
# print( a.intersection(b))
# print( a.union(b))
# print( a.difference(b))
# print( b.difference(a))
# print( a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# c = {1, 2}
# print(c.issubset(a))
# print(a.issuperset(c))
# print( 1 in a)
# print( 6 in a)
# print( len(a))
# print(len(b))

# Sets versus multisets
# setA = {'a','b','b','c'}
# print(setA)
# listA = ['a','b','b','c']
# print(listA)

# from collections import Counter
# counterA = Counter(['a','b','b','c'])
# print(counterA)
# print(Counter({'b': 2, 'a': 1, 'c': 1}))

#Chapter 9: Simple Mathematical Operators

# Division
# import operator 
# a, b, c, d, e = 3, 2, 2.0, -3, 10
# # d = operator.div(a, b)
# print(d)
# c = operator.__div__(a, b)
# print(c)

#Addition
# a, b = 1, 2
# print(a + b)
# import operator 
# operator.add(a, b)
# a = operator.iadd(a, b)
# print(a)

# Exponentiation
# a, b = 2, 3
# print((a ** b))
# print(pow(a, b))
# import math
# print(math.pow(a, b))
# import operator
# print(operator.pow(a, b))

# import math
# import cmath
# c = 4
# print(math.sqrt(c))
# print(cmath.sqrt(c))

# import math
# x = 8
# print(math.pow(x, 1/3))
# print(x**(1/3))

#Trigonometric Functions
# a, b = 1, 2
# import math
# print(math.sin(a))
# print(math.cosh(b))
# print(math.atan(math.pi))
# print(math.hypot(a, b))

#Inplace Operations
# a=1
# a = a + 1
# print(a)
# a = a * 2
# print(a)

# #Subtraction
# a, b = 1, 2
# print(b - a)
# import operator 
# print(operator.sub(b, a))

# Multiplication
# a, b = 2, 3
# print(a * b)
# import operator
# print(operator.mul(a, b))

# Logarithms
# import math
# import cmath
# print(math.log(5))
# print(math.log(5, math.e)) 
# print(cmath.log(5))
# print(math.log(1000, 10))
# print(cmath.log(1000, 10))

#Modulus
# print(3 % 4)
# print(10 % 2)
# print(6 % 4)
# import operator
# print(operator.mod(3 , 4))
# print(operator.mod(10 , 2))
# print(operator.mod(6 , 4))

#Chapter 10: Bitwise Operators

#Bitwise NOT
# print(~0)
# print(~-0)
# print(~-1)

# # Bitwise XOR (Exclusive OR)
# print(60 ^ 30)
# print(bin(60 ^ 30))

# Bitwise AND
# a = 60 & 30
# print(a)
# print(bin(60 & 30))

#Bitwise OR
# print(60 | 30)
# print(bin(60 | 30))

#Bitwise Left Shift
# print(2 << 2)
# print(bin(2 << 2))

# Bitwise Right Shift
# print(8 >> 2)
# print(bin(8 >> 2))

# Inplace Operations

# a = 0b001
# a &= 0b010
# print(a)
# a = 0b001
# a |= 0b010
# print(a)
# a = 0b001
# a <<= 2
# print(a)
# a = 0b100
# a >>= 2
# print(a)
# a = 0b101
# a ^= 0b011
# print(a)

#Boolean Operators
#`and` and `or` are not guaranteed to return a boolean

# def or_(a, b):
#     if a:
#         return a
#     else:
#         return b
# print(or_(2,5))

# def and_(a, b):
#     if not a:
#         return a
#     else:
#         return b
# print(and_(2,5))

#A simple example
# x=3.141
# if 3.14 < x < 3.142:
#     print("x is near pi")

# def true_func():
#     print("true_func()")
#     return True

# def false_func():
#     print("false_func()")
#     return False

# true_func() or false_func()
# print(true_func())

# false_func() or true_func()
# print(false_func())
# print(true_func())

# true_func() and false_func()
# print(true_func())
# print(false_func())

# false_func() and false_func()
# print(false_func())


