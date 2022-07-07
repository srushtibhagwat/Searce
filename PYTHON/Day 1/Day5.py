#Chapter 38: Classes

#Bound, unbound, and static methods
# class A(object): 
#     def f(self, x):
#         #print("This is the method")
#         return 2 * x
# a = A()
# A.f(a, 20)

# import inspect
# print(inspect.isfunction(A.f) )
# print(inspect.ismethod(A.f))

# class D(object): 
#     multiplier = 2
#     @classmethod 
#     def f(cls, x):
#         return cls.multiplier * x
#     @staticmethod 
#     def g(name):
#         print("Hello, %s" % name)
# print(D.f)
# print(D.f(12))
# print(D.g("world"))

# d = D()
# d.multiplier = 1337
# print((D.multiplier, d.multiplier))
# print(d.f)

# Basic inheritance
# class BaseClass(object): 
#     pass
# class DerivedClass(BaseClass): 
#     pass

# class Rectangle():
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def area(self):
#         return self.w * self.h
#     def perimeter(self):
#         return 2 * (self.w + self.h)

# class Square(Rectangle): 
#     def __init__(self, s):
#         # call parent constructor, w and h are both s
#         super(Square, self).__init__(s, s)
#         self.s = s
# r = Rectangle(3, 4)
# s = Square(2)
# print(r.area())
# print(s.area())
# print(s.perimeter())
# print(issubclass(Square, Rectangle) )
# print(isinstance(r, Rectangle) )

# Monkey Patching
# class A(object):
#     def __init__(self, num):
#         self.num = num
#     def __add__(self, other):
#         return A(self.num + other.num)
#     def get_num(self): 
#         return self.num
# #A.get_num = get_num()
# foo = A(42)
# bar = A(6); 
# print(foo.get_num())
# print(bar.get_num())

#Class methods: alternate initializers
# class Person(object):
#     def __init__(self, first_name, last_name, age): 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + " " + last_name
#     @classmethod
#     def from_full_name(cls, name, age):
#         if " " not in name: 
#             raise ValueError
#         first_name, last_name = name.split(" ", 2) 
#         return cls(first_name, last_name, age)
#     def greet(self):
#         print("Hello, my name is " + self.full_name + ".")
# bob = Person("Bob", "Bobberson", 42)
# alice = Person.from_full_name("Alice Henderson", 31)
# print(bob.greet())
# print(alice.greet())

#Multiple Inheritance
# class Foo(object):
#     foo = 'attr foo of Foo'
# class Bar(object):
#     foo = 'attr foo of Bar' 
# class FooBar(Foo, Bar):
#     foobar = 'attr foobar of FooBar'
# fb = FooBar()
# print(fb.foo)
# print(FooBar.mro())

# class Foo(object):
#     def __init__(self):
#         print ("foo init")
# class Bar(object):
#     def __init__(self):
#         print ("bar init")
# class FooBar(Foo, Bar): 
#     def __init__(self):
#         print ("foobar init" )
#         super(FooBar, self).__init__()
# a = FooBar()
# print (isinstance(a,FooBar) )
# print (isinstance(a,Foo))
# print (isinstance(a,Bar))

#Properties
# class MyClass(object): 
#     def __init__(self):
#        self._my_string = ""
#     def string(self):
#         """A profoundly important string."""
#         return self._my_string
#     def string(self, new_value):
#         assert isinstance(new_value, str), \
#             "Give me a string, not a %r!" % type(new_value)
#         self._my_string = new_value
#     def x(self):
#         self._my_string = None
# mc = MyClass() 
# mc.string = "String!" 
# print(mc.string)
# del mc.string

#Default values for instance variables
# class Rectangle(object):
#     def __init__(self, width, height, color='blue'):
#         self.width = width
#         self.height = height
#         self.color = color
#     def area(self):
#         return self.width * self.height
# default_rectangle = Rectangle(2, 3) 
# print(default_rectangle.color) # blue
# red_rectangle = Rectangle(2, 3, 'red') 
# print(red_rectangle.color) # red

# class Rectangle2D(object):
#     def __init__(self, width, height, pos=[0,0], color='blue'):
#         self.width = width
#         self.height = height
#         self.pos = pos
#         self.color = color
# r1 = Rectangle2D(5,3)
# r2 = Rectangle2D(7,8)
# r1.pos[0] = 4
# print(r1.pos) 
# print(r2.pos)   

# class Rectangle2D(object):
#     def __init__(self, width, height, pos=None, color='blue'):
#         self.width = width
#         self.height = height
#         self.pos = pos or [0, 0] 
# r1 = Rectangle2D(5,3)
# r2 = Rectangle2D(7,8)
# r1.pos[0] = 4
# print(r1.pos )
# print(r2.pos)

#Class and instance variables
# class D:
#     x = []
#     def __init__(self, item):
#         self.x.append(item) 
# d1 = D(1)
# d2 = D(2)
# print(d1.x)
# print(d2.x)
# print(D.x)

#Class composition
# class Country(object): 
#     def __init__(self):
#         self.cities=[]
#     def addCity(self,city): 
#         self.cities.append(city)

# class City(object):
#     def __init__(self, numPeople):
#         self.people = []
#         self.numPeople = numPeople
#     def addPerson(self, person): 
#         self.people.append(person)
#     def join_country(self,country): 
#         self.country = country 
#         country.addCity(self)
#         for i in range(self.numPeople): 
#             Person(i).join_city(self)

# class Person(object):
#     def __init__(self, ID):
#         self.ID=ID
#     def join_city(self, city): 
#         self.city = city 
#         city.addPerson(self)
#     def people_in_my_country(self):
#         x= sum([len(c.people) for c in self.city.country.cities]) 
#         return x
# US=Country()
# NYC=City(10).join_country(US)
# SF=City(5).join_country(US)
# print(US.cities[0].people[0].people_in_my_country())

#Listing All Class Members
# print(dir(list))

#Singleton class
# class Singleton:
#     def __new__(cls):
#         try:
#             it = cls.__it__
#         except AttributeError:
#             it = cls.__it__ = object.__new__(cls)
#         return it
#     def __repr__(self):
#         return '<{}>'.format(self.__class__.__name__.upper())
#     def __eq__(self, other): 
#         return other is self

#Chapter 40: String Formatting

#Basics of String Formatting
# foo = 1
# bar = 'bar'
# baz = 3.14
# print('{}, {} and {}'.format(foo, bar, baz))
# print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz)) 
# print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

# class AssignValue(object):
#     def __init__(self, value):
#         self.value = value
# my_value = AssignValue(6)
# print('My value is: {0.value}'.format(my_value))

# my_dict = {'key': 6, 'other_key': 7}
# print("My other key is: {0[other_key]}".format(my_dict)) 

# my_list = ['zero', 'one', 'two']
# print("2nd element is: {0[2]}".format(my_list))

# number_list = [12,45,78]
# print(map('the number is {}'.format, number_list))

# from datetime import datetime,timedelta 
# once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
# delta = timedelta(days=13, hours=8, minutes=20)
# gen = (once_upon_a_time + x * delta for x in range(5))
# print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))

#Format literals (f-string)
# foo = 'bar'
# print(f'Foo is {foo}')
# print(f'{foo:^7s}')

# price = 478.23
# print(f"{f'${price:0.2f}':*>20s}")

# def fn(l, incr):
#     result = l[0]
#     l[0] += incr
#     return result 
# lst = [0]
# print(f'{fn(lst,2)} {fn(lst,3)}')
# print(f'{fn(lst,2)} {fn(lst,3)}')
# print(lst)

#Float formatting
# print('{0:.0f}'.format(42.12345))
# print('{0:.1f}'.format(42.12345))
# print('{0:.3f}'.format(42.12345))

# print('{:.3f}'.format(42.12345))

# print('{0:.0%}'.format(42.12345))

# s = 'Hello'
# a, b, c = 1.12345, 2.34567, 34.5678
# digits = 2
# print('{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits))

#Named placeholders
# data = {'first': 'Hodor', 'last': 'Hodor!'}
# print('{first} {last}'.format(**data))
# print('{first} {last}'.format_map(data))

#String formatting with datetime
# from datetime import datetime
# print('North America: {dt:%m/%d/%Y}. ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()))

#Formatting Numerical Values
# print('{:c}'.format(65))
# print('{:d}'.format(0x0a))
# print('{0:X}'.format(10) )
# r, g, b = (1.0, 0.4, 0.0)
# print('#{:02X}{:02X}{:02X}'.format(int(255 * r), int(255 * g), int(255 * b)))

#Nested formatting
# print('{:.>10}'.format('foo'))
# print('{:.>{}}'.format('foo', 10))
# data = ["a", "bbbbbbb", "ccc"]
# m = max(map(len, data))
# for d in data:
#     print('{:>{}}'.format(d, m))

#Chapter 41: String Methods
#Changing the capitalization of a string
# print("This is a 'string'.".upper())
# print("This IS a 'string'.".lower())
# print("this Is A 'String'.".capitalize())
# print( "this Is a 'String'".title())
# print("this iS A STRiNG".swapcase())
# print(map(str.upper,["These","are","some","'strings'"]))

#str.format and f-strings: Format values into a string
# i = 10
# f = 1.5
# s = "foo"
# l = ['a', 1, 2]
# d = {'a': 1, 2: 'foo'}
# # print("10 1.5 foo ['a', 1, 2] {'a': 1, 2: 'foo'}")
# # print(str.format("{} {} {} {} {}", i, f, s, l, d))
# print(f"{i} {f} {s} {l} {d}")
# print(f"{i:d} {f:0.1f} {s} {l!r} {d!r}")

#String module's useful constants   

# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print( string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)
# print(string.whitespace)
# print(string.printable)

#Stripping unwanted leading/trailing characters from a string
# print("    a line with leading and trailing space     ".strip())
# print(" a Python prompt".strip('> '))
# print("     spacious string      ".rstrip())
# print("     spacious string      ".rstrip())

#Reversing a string
# print(reversed('hello'))
# print([char for char in reversed('hello')])
# print(''.join(reversed('hello')))

#Split a string based on a delimiter into a list of strings
# print("This is a sentence.".split())
# print(" This is    a sentence.  ".split())
# print("            ".split())
# print("This is a sentence.".split(' '))
# print("Earth,Stars,Sun,Moon".split(','))
# print("This is a sentence.".split('e', maxsplit=0))
# print("This is a sentence.".split('e', maxsplit=1))
# print("This is a sentence.".split('e', maxsplit=2))
# print("This is a sentence.".split('e', maxsplit=-1))
# print("This is a sentence.".rsplit('e', maxsplit=1))
# print("This is a sentence.".rsplit('e', maxsplit=2))

#Replace all occurrences of one substring with another substring
# print("Make sure to foo your sentence.".replace('foo', 'spam'))
# print( "It can foo multiple examples of foo if you want.".replace('foo', 'spam'))

#Testing what a string is composed of
# print("Hello World".isalpha())
# print("Hello2World".isalpha())
# print("HeLLO WORLD".isupper())
# print("".isupper())
# print("Hello world".islower())
# print("Hello World".istitle())
# print("Hello2World".isalnum())
# print("HelloWorld".isalnum())
# print("2016".isalnum())
# print(" ".isspace())

# my_str = ''
# print(my_str.isspace())
# print(my_str.isspace() or not my_str)
# print(not my_str.strip())

#String Contains
# print("foo" in "foo.baz.bar")
# print("" in "test")

#Join a list of strings into one string
# print(" ".join(["once","upon","a","time"]))
# print("---".join(["once", "upon", "a", "time"]))

#Counting number of times a substring appears in a string
# s = "She sells seashells by the seashore."
# print(s.count("sh"))
# print(s.count("se"))
# print(s.count("sea"))
# print(s.count("sea", start))

#Case insensitive string comparisons
# print("ß".lower())
# print("ß".upper().lower())
# print(help(str.casefold))
# print("ê" == "ê")

#Test the starting and ending characters of a string
# s = "This is a test string"
# print(s.startswith("T"))
# print(s.startswith("Thi"))
# print(s.startswith("thi"))
# print( s.startswith("is", 2))
# print(s.startswith(('This', 'That')))
# print(s.startswith(('ab', 'bc')))
# s = "this ends in a full stop."
# print(s.endswith('.'))
# print(s.endswith('!'))
# print(s.endswith('stop.'))
# print(s.endswith(('.', 'something')))
# print(s.endswith(('ab', 'bc')))

#Chapter 42: Using loops within functions
# def func(params):
#     for value in params:
#         print ('Got value {}'.format(value))
#         if value == 1:
#             print(">>>> Got 1")
#             return
#         print ("Still looping") 
#     return "Couldn't find 1"
# func([5, 3, 1, 2, 8, 9])

#Chapter 43: Importing modules

#Importing a module
# import random
# print(random.randint(1, 10))

# import random as rn
# print(rn.randint(1, 10))

# from math import sin 
# print(sin(1))

#Importing all names from a module
# from math import *
# print(sqrt(2) )
# print(ceil(2.7))

# def sqrt(num):
#     print("I don't know what's the square root of {}.".format(num))
#     print(sqrt(4))
# from math import * 
# print(sqrt(4))

#Programmatic importing
# import importlib
# random = importlib.import_module("random")
# print(random)

#PEP8 rules for Imports
# from math import sqrt, ceil
# from math import sqrt 
# from math import ceil

#Importing specific names from a module
# from random import randint  
# print(randint(1, 10))

# from math import pi
# print(pi)

# import random 
# a = random.randrange(1, 10)
# print(a)

#Importing submodules
#from module.submodule import function

#Re-importing a module
# import math
# math.pi = 3 
# print(math.pi)
# import math 
# print(math.pi)
# print(math.pi) 
# import sys
# if 'math' in sys.modules: 
#     del sys.modules['math']  
# import math   
# print(math.pi)

# import math
# math.pi = 3
# print(math.pi) 
# from importlib import reload 
# reload(math)
# print(math.pi)

#Chapter 44: Dierence between Module and Package
#module.py
# def hi():
#     print("Hello world!")
# #my_script.py
# import module 
# module.hi()
# from module import hi 
# hi()

# # Packages
# from package.dog import woof 
# from package.hi import hi
# #dog.py
# def woof(): 
#     print("WOOF!!!")
# #hi.py
# def hi():
#     print("Hello world!")

#Chapter 45: Math Module
#Rounding: round, floor, ceil, trunc
# x = 1.55
# y = -1.55
# print(round(y))
# print(round(x))

import math
# print(math.floor(x))
# print(math.floor(y))

# print(math.ceil(x))
# print(math.ceil(y))

# print(math.trunc(x) )
# print(math.trunc(y))

#Trigonometry
# print(math.hypot(2,4))
# print( math.radians(45))
# print(math.degrees(math.asin(1)))
# print(math.sin(math.pi / 2))
# print(math.sin(math.radians(90)))
# print(math.cos(math.pi / 2))
# print(math.acos(1))
# print(math.atan(math.inf))
# print(math.atan2(1, 2))
# print(math.atan2(-1, -2))
# print(math.sinh(math.pi))
# print(math.asinh(1))
# print(math.cosh(math.pi))
# print(math.acosh(1))
# print(math.tanh(math.pi))
# print(math.atanh(0.5))

#Pow for faster exponentiation
# from math import pow 
# print(pow(5,5))

#Infinity and NaN ("not a number")
# pos_inf = math.inf
# neg_inf = -math.inf
# not_a_num = math.nan
# print( pos_inf, neg_inf, not_a_num)
# print(math.isinf(pos_inf))
# print(math.isinf(neg_inf))
# pos_inf == float('inf')
# neg_inf == float('-inf')
# neg_inf == pos_inf
# print(math.isfinite(pos_inf))
# print(math.isfinite(0.0))

#Logarithms
# print(math.log(math.e) )
# print(math.log(1) )
# print(math.log(100))

#Constants
# from math import pi, e 
# print(pi)
# print(e)

# Copying signs
# print(math.copysign(-2, 3) )
# print(math.copysign(3, -3) )
# print(math.copysign(4, 14.2) )
# print(math.copysign(1, -0.0))

#Chapter 46: Complex math

#Advanced complex arithmetic
# import cmath
# z = 2+3j 
# print(cmath.phase(z))

# print(cmath.polar(z)) 
# print(cmath.rect(2, cmath.pi/2))

# print(cmath.exp(z) )
# print(cmath.log(z) )
# print(cmath.log10(-100))

# print(cmath.sqrt(z))

# print(cmath.sin(z))
# print(cmath.cos(z))
# print(cmath.tan(z))
# print(cmath.asin(z))
# print(cmath.acos(z))
# print(cmath.atan(z))
# print(cmath.sin(z)**2 + cmath.cos(z)**2)

# #Basic complex arithmetic
# z = 2+3j 
# w = 1-7j

# print(z + w )
# print(z - w )
# print(z * w )
# print(z / w )
# print(z**3)

# print(z.real )
# print(z.imag )
# print(abs(z))
# print(z.conjugate())