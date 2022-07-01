#chapter 1:
# Creating variables and assigning values

# Integer
# _a= 2
# print(_a)
# b = 9223372036854775807 
# print(b)

# # Floating point
# pi = 3.14 
# print(pi)

# # String
# s = 'A' 
# print(s)
# name = 'TIGER' 
# print(name)

# # Boolean
# q = True 
# print(q)

# # Empty value or null data type
# x = None
# print(x)

# #Types
# _a=2
# print(type(_a))

# b = 9223372036854775807 
# print(type(b))

# pi = 3.14 
# print(type(pi))

# c = 'A'
# print(type(c))

# name = 'TIGER' 
# print(type(name))

# q = True 
# print(type(q))

# z= None
# print(type(z))

# a, b, c = 1, 2, 3 
# print(a, b, c)

# a, b, _ = 1, 2, 3 
# print(a, b) #NO of values and No of underscores should be equal

# a = b = c = 1 
# print(a,b,c)
# b = 2 
# print(a,b,c)

# x = y = [7, 8, 9] #It is also true about mutable types
# x = [13, 8, 9] 
# print(y)

# x = y = [7, 8, 9]
# x[0] = 13 
# print(y)

# x = [1, 2, [3, 4, 5], 6, 7] # Nested loop is also valid
# print (x[2][1])

# a=2 
# print(a)
# # Output: 2
# a = "New value" 
# print(a) #we can assign A NEW VALUE BY = operator whenver we want

#Block Indentation

# def my_function(): 
#     a = 2
#     return a
# print(my_function())

# a = 3
# b = 5
# if a > b: print(a)
# else: print(b)

# def a(): #It works with the empty block with the help of pass
#      pass

#Built-in Types 

#Booleans
# print(issubclass(bool, int))
# print(isinstance(True, bool))
# print(isinstance(False, bool))
# print(True + False == 1)
# print(True * True == 1)

#Numbers

#integers
# a=2
# print(type(a))
# b = 100
# c = 123456789
# d = 38563846326424324

# #float
# a = 2.0
# print(type(a))
# b = 100.e0
# print(type(b))
# c = 123456789.e1

# #Complex numbers
# a = 2 + 1j
# print(type(a))
# b = 100 + 10j

#Sequences and collections

#list
# a = [1, 2, 3]
# print(type(a))
# b = ['a', 1, 'python', (1, 2), [1, 2]] 
# print(type(b))
# b[2] = 'something else'
# print(type(b[2])) #this is a string and not a list

#set 
# a = {1, 2, 'a'}
# print(type(a))

#dictionary
# a = {1: 'one',2: 'two'}
# print(type(a))
# b = {'a': [1, 2, 3],'b': 'a string'}
# print(type(b))

#testing the type of variables
# a = '123'
# print(type(a))
# b = 123 
# print(type(b))

#Mutable and Immutable Data Types
# def f(m):
#     m.append(3)
# x = [1, 2]
# f(x)
# x == [1, 2]
# print(x)

# Collection Types

#list
# names = ['Alice', 'Bob', 'Craig', 'Diana', 'adam'] 
# print(names[0]) 
# print(names[2])
# print(type(names))
# print(names[-1])
# print(names[-4])

# names = ['Alice', 'Bob', 'Craig', 'Diana', 'adam'] 
# names.append("Ram")
# print(names)

# names.insert(1, "Siya")
# print(names)

# names.remove("Ram")
# print(names)

# print(names.index("Alice"))
# print(len(names))

# a = [1, 1, 1, 2, 3, 4]
# print(a.count(1))

# print(a.reverse())#or
# print(a[::-1]) #we can do this using slice operator also

#Tuple
# ip_address = ('10.20.30.40', 8080)
# print(type(ip_address))

#set
# first_names = {'Adam', 'Beth', 'Charlie'}
# print(type(first_names))
# my_list = [1,2,3]
# print(type(my_list))
# my_set = set(my_list)
# print(type(my_set))

#defaultdict
# from collections import defaultdict
# state_capitals = defaultdict(lambda: 'Boston')
# print(state_capitals)

#User Input
# name = input("What is your name? ")
# print(name)

#Built in Modules and Functions
# x = pow(2,3)
# print(x)
# y = help(max)
# print(y)
# import math
# print(math.sqrt(16))
# print(dir(math))

#Creating a module
# def say_hello(): 
#     print("Hello!")

# say_hello()

# import hello
# hello.say_hello()

# if __name__ == '__main__':
#     from hello import say_hello 
#     say_hello()

#String function - str() and repr()
# import datetime
# today = datetime.datetime.now()
# print(str(today) )
# print(repr(today))

# Help Utility
# import math
# help(math)

#-------------------------------------------------------------------------------------------------

#Chapter 2:

#Python Data Types

# String Data Type
# a_str = 'Hello World'
# print(a_str) 
# print(a_str[0]) 
# print(a_str[0:5])

# Set Data Types
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} 
# print(basket)
# a = set('abracadabra')
# print(a) 
# a.add('z')
# print(a)

#Numbers data type
# int_num = 10 
# print(int_num)
# print(type(int_num))
# float_num = 10.2
# print(float_num)
# print(type(float_num))
# complex_num = 3.14j
# print(complex_num)
# print(type(complex_num))

# #List Data Type
# list = [123,'abcd',10.2,'d']
# print(list) 
# print(list[0:2])
# print(list * 2)

#Dictionary Data Type
# dic={'name':'red','age':10}
# print(dic) 
# print(dic['name']) 
# print(dic.values()) 
# print(dic.keys())

# Tuple Data Type
# tuple = (123,'hello')
# tuple1 = ('world')
# print(tuple)
# print(tuple[0])

#-------------------------------------------------------------------------------------------------

#Chapter 3:

#Comments and Documentation

#Single line, inline and multiline comments
print("Hello World") #Print HELLO WORLD
"""
multiple lines comments

"""

#Programmatically accessing docstrings
def func():
    """This is a function that does nothing at all""" 
    return

print(func.__doc__)
