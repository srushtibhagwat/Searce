#Chapter 47: Collections module

#collections.Counter
# import collections
# c = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})
# print(c['a'])
# collections.Counter('Happy Birthday')
# c['c'] = -3
# print(c)
# print(list(c.elements()))
# print(c - collections.Counter())
# c.clear()
# print(c)

#collections.OrderedDict
# d = {'foo': 5, 'bar': 6}
# print(d)
# d['baz'] = 7
# print(d)
# d['foobar'] = 8
# print(d)

# from collections import OrderedDict
# o = OrderedDict()
# o['key1'] = "value1"
# o['key2'] = "value2"
# print(o)

#collections.defaultdict
# state_capitals = collections.defaultdict(str) 
# print(state_capitals)

# print(str())
# print(int())
# print(list)

# fruit_counts = collections.defaultdict(int)
# fruit_counts['apple'] += 2 
# print(fruit_counts)
# print(fruit_counts['banana'])
# print(fruit_counts)

# state_capitals['Alabama'] = 'Montgomery'
# print(state_capitals)

#collections.namedtuple
# Person = collections.namedtuple('Person', ['age', 'height', 'name'])
# jack = Person(age=30, height=178, name='Jack S.')
# print(jack.age) 
# print(jack.name)

# Human = collections.namedtuple('Person',  'age, height, name')
# dave = Human(30, 178, 'Dave')
# print(dave)

#Chapter 48: Operator module

#Itemgetter
# from itertools import groupby 
# from operator import itemgetter 
# adict = {'a': 1, 'b': 5, 'c': 1}
# a = dict((i, dict(v)) for i, v in groupby(adict.items(), itemgetter(1)))
# print(a)
# alist_of_tuples = [(5,2), (1,3), (2,2)] 
# c = sorted(alist_of_tuples, key=itemgetter(1,0))
# print(c)

# #Operators as alternative to an infix operator
# print(1+1)
# from operator import add 
# a = add(1, 1)
# print(a)

# from operator import mul 
# print(mul('a', 10))
# print(mul([3], 3))

#Methodcaller
# alist = ['wolf', 'sheep', 'duck']
# ANS = list(filter(lambda x: x.startswith('d'), alist))
# print(ANS)
# from operator import methodcaller
# a = list(filter(methodcaller('startswith', 'd'), alist))
# print(a)

#Chapter 49: JSON Module

#Storing data in a file
# import json
# d={
#     'foo': 'bar',
#     'alice': 1,
#     'wonderland': [1, 2, 3]
# }
# with open(filename, 'w') as f: 
#     json.dump(d, f)

# #Retrieving data from a file
# import json
# with open(filename, 'r') as f: 
#     d = json.load(f)

#Formatting JSON output
# data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
# print(json.dumps(data))

#`load` vs `loads`, `dump` vs `dumps`
# import json
# data = {u"foo": u"bar", u"baz": []} 
# json_string = json.dumps(data)
# print(json.loads(json_string))

# import json
# from io import StringIO
# json_file = StringIO()
# data = {u"foo": u"bar", u"baz": []}
# json.dump(data, json_file)
# print(json_file.seek(0) )
# json_file_content = json_file.read()
# print(json_file.seek(0) )
# print(json.load(json_file))

#JSON encoding custom object
# import json
# from datetime import datetime
# data = {'datetime': datetime(2016, 9, 26, 4, 44, 0)} 
# print(json.dumps(data)) #we get an error here

# import json
# class DatetimeJSONEncoder(json.JSONEncoder): 
#     def default(self, obj):
#         try:
#             return obj.isoformat()
#         except AttributeError:
#             return super(DatetimeJSONEncoder, self).default(obj)

# encoder = DatetimeJSONEncoder() 
# print(encoder.encode(data))

#Creating JSON from Python dict
# import json 
# d={
#     'foo': 'bar',
#     'alice': 1,
#     'wonderland': [1, 2, 3]
# }
# print(json.dumps(d))

#Creating Python dict from JSON
# import json
# s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}' 
# print(json.loads(s))

#Chapter 50: Sqlite3 Module

#Sqlite3 - Not require separate server process
# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE stocks
#          (date text, trans text, symbol text, qty real, price real)''')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)") 
# conn.commit()
# conn.close()

#Chapter 51: The os Module

#makedirs - recursive directory creation
import os
# os.makedirs("./dir2/subdir1")
# os.makedirs("./dir2/subdir2")

#Create a directory
# os.mkdir('newdir')

#Get current directory
# print(os.getcwd())

#Determine the name of the operating system
# print(os.name)

#Remove a directory
# os.rmdir(path) #any path

#Chapter 52: The locale Module

#Currency Formatting US Dollars Using the locale Module
# import locale 
# locale.setlocale(locale.LC_ALL, '')
# Out[2]: 'English_United States.1252'
# locale.currency(762559748.49)
# Out[3]: '$762559748.49'
# locale.currency(762559748.49, grouping=True)
# Out[4]: '$762,559,748.49'

#Chapter 53: Itertools Module

#Combinations method in Itertools Module
# a = [1,2,3,4,5]
# b = list(itertools.combinations(a, 2)) 
# print(b)

#itertools.dropwhile
# def is_even(x): 
#     return x % 2 == 0
# lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
# result = list(itertools.dropwhile(is_even, lst))
# print(result)

#Zipping two iterators until they are both exhausted
# from itertools import zip_longest
# a = [i for i in range(5)] 
# b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']     
# for i in zip_longest(a, b):
#     x, y = i 
#     print(x, y)

#Take a slice of a generator
# results = fetch_paged_results() 
# limit = 20 
# for data in itertools.islice(results, limit):
#     print(data)

# import itertools
# def gen(): 
#     n=0
#     while n < 20: 
#         n += 1
#     yield n
# for part in itertools.islice(gen(), 3): 
#     print(part)

#Grouping items from an iterable object using a function
# lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
# def testGroupBy(lst):
#     groups = itertools.groupby(lst, key=lambda x: x[1]) 
#     for key, group in groups:
#         print(key, list(group)) 
        
# testGroupBy(lst)

# groups = itertools.groupby(lst, key=lambda x: x[1])
# for key, group in sorted((key, list(group)) for key, group in groups):
#     print(key, list(group))

# itertools.takewhile
# def is_even(x): 
#     return x % 2 == 0
# lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
# result = list(itertools.takewhile(is_even, lst))
# print(result)

# itertools.permutations
# a = [1,2,3]
# print(list(itertools.permutations(a)))

# print(list(itertools.permutations(a, 2)))

#itertools.repeat
# import itertools
# for i in itertools.repeat('over-and-over', 3):
#     print(i)

#Get an accumulated sum of numbers in an iterable
# import itertools as it 
# import operator
# print(list(it.accumulate([1,2,3,4,5])))
# print(list(it.accumulate([1,2,3,4,5], func=operator.mul)))

#Cycle through elements in an iterator
# import itertools as it 
# print(it.cycle('ABCD'))

#itertools.product
# for x, y in itertools.product(xrange(10), xrange(10)): 
#     print (x, y)

#itertools.count
# for number in itertools.count(): 
#     if number > 20:
#         break 
#     print(number)

#Chaining multiple iterators together
# from itertools import chain
# a = (x for x in ['1', '2', '3', '4']) 
# b = (x for x in ['x', 'y', 'z'])
# print(' '.join(chain(a, b)))

#Chapter 54: Asyncio Module

#Coroutine and Delegation Syntax
# import asyncio
# async def cor1(): 
#     print("cor1 start") 
#     for i in range(10):
#         await asyncio.sleep(1.5) 
#         print("cor1", i)
# async def cor2(): 
#     print("cor2 start") 
# #     for i in range(15):
#         await asyncio.sleep(1)
#         print("cor2", i)
# loop = asyncio.get_event_loop()
# cors = asyncio.wait([cor1(), cor2()])
# loop.run_until_complete(cors)

#Asynchronous Executors
# import asyncio
# from concurrent.futures import ThreadPoolExecutor
# def func(a, b):
#     return a+b
# async def main(loop):
#     result = await loop.run_in_executor(None, func, "Hello,", " world!") 
#     print(result)
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop() 
#     loop.set_default_executor(ThreadPoolExecutor()) 
#     loop.run_until_complete(main(loop))

#Using UVLoop
# import asyncio 
# import uvloop
# if __name__ == "__main__": 
#     asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) 
#     loop = asyncio.new_event_loop()

#Synchronization Primitive: Event
# import asyncio
# def trigger(event):
#     print('EVENT SET')
#     event.set() 
# async def consumer_a(event):
#     consumer_name = 'Consumer A'
#     print('{} waiting'.format(consumer_name)) 
#     await event.wait()
#     print('{} triggered'.format(consumer_name))
# async def consumer_b(event):
#     consumer_name = 'Consumer B'
#     print('{} waiting'.format(consumer_name)) 
#     await event.wait()
#     print('{} triggered'.format(consumer_name))
# event = asyncio.Event()
# main_future = asyncio.wait([consumer_a(event),consumer_b(event)])
# event_loop = asyncio.get_event_loop()
# event_loop.call_later(0.1, functools.partial(trigger, event))
# done, pending = event_loop.run_until_complete(main_future)

#A Simple Websocket
# import asyncio 
# import aiohttp
# session = aiohttp.ClientSession() 
# class EchoWebsocket:
#     async def connect(self):
#         self.websocket = await session.ws_connect("wss://echo.websocket.org")
#     async def send(self, message): 
#         self.websocket.send_str(message)
#     async def receive(self):
#         result = (await self.websocket.receive()) 
#         return result.data
# async def main():
#     echo = EchoWebsocket()
#     await echo.connect()
#     await echo.send("Hello World!") 
#     print(await echo.receive())
# if __name__ == '__main__': 
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

#Chapter 55: Random module

# import string
# alphabet = string.ascii_letters + string.digits 
# while True:
#     password = ''.join(choice(alphabet) for i in range(10)) 
#     if (any(c.islower() for c in password)
#         and any(c.isupper() for c in password)
#         and sum(c.isdigit() for c in password) >= 3): 
#         break

#Create cryptographically secure random numbers
# from random import SystemRandom 
# secure_rand_gen = SystemRandom()
# print([secure_rand_gen.randrange(10) for i in range(10)])
# print(secure_rand_gen.randint(0, 20))

#Random and sequences: shue, choice and sample
# import random
# laughs = ["Hi", "Ho", "He"]
# random.shuffle(laughs) #
# print(laughs)
# print(random.choice(laughs))
# print(random.sample( laughs , 1 ))
# print(random.sample(laughs, 3))

#Creating random integers and floats: randint, randrange, random, and uniform
import random
# print(random.randint(1, 8))
# print(random.randrange(100) )
# print(random.randrange(20, 50) )
# print(random.rangrange(10, 20, 3))

# print(random.random())
# print(random.uniform(1, 8))

#Reproducible random numbers: Seed and State
# random.seed(5)  
# print(random.randrange(0, 10)) 
# print(random.randrange(0, 10))

# random.seed(5) 
# print(random.randrange(0, 10))
# print(random.randrange(0, 10))

#Random Binary Decision
# import random
# probability = 0.3
# if random.random() < probability: 
#     print("Decision with probability 0.3")
# else:
#     print("Decision with probability 0.7")

#Chapter 56: Functools Module

#partial
# from functools import partial
# unhex = partial(int, base=16)
# unhex.__doc__ = 'Convert base16 string to int'
# print(unhex('ca11ab1e'))

#cmp_to_key
# import functools
# import locale
# print(sorted(["A", "S", "F", "D"], key=functools.cmp_to_key(locale.strcoll)))

#lru_cache
# def fibonacci(n):
#     if n < 2: 
#         return n
#     return fibonacci(n-1) + fibonacci(n-2) 
    
# print(fibonacci(15))

#total_ordering
# class Employee:
#     def __eq__(self, other):
#         return ((self.surname, self.name) == (other.surname, other.name))
#     def __lt__(self, other):
#         return ((self.surname, self.name) < (other.surname, other.name))
    
# #reduce
# from functools import reduce 
# def factorial(n):
#     return reduce(lambda a, b: (a*b), range(1, n+1))

# print(factorial(2))