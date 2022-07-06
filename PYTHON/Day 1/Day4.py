# Chapter 24: Linked lists

# Single linked list example
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None
#     def getData(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setData(self, val):
#         self.data = val
#     def setNext(self, val):
#         self.next = val
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def isEmpty(self):
#         return self.head is None
#     def add(self, item):
#         new_node = Node(item)
#         new_node.setNext(self.head)
#         self.head = new_node
#     def size(self):
#         count = 0
#         current = self.head
#         while current is not None: 
#             count += 1
#             current = current.getNext()
#         return count
#     def search(self, item):
#         current = self.head
#         found = False
#         while current is not None and not found:
#             if current.getData() is item:
#                 found = True
#             else:
#                 current = current.getNext()
#         return found
#     def remove(self, item):
#         current = self.head
#         previous = None
#         found = False
#         while current is not None and not found:
#             if current.getData() is item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getNext()
#         if found:
#             if previous is None:
#                 self.head = current.getNext()
#             else:
#                 previous.setNext(current.getNext())
#         else:
#             raise ValueError
#             print ('Value not found.')
#     def insert(self, position, item):
#         if position > self.size() - 1:
#             raise IndexError
#             print ("Index out of bounds.")
#         current = self.head
#         previous = None
#         pos = 0
#         if position == 0:
#             self.add(item)
#         else:
#             new_node = Node(item)
#             while pos < position:
#                 pos += 1
#                 previous = current
#                 current = current.getNext()
#             previous.setNext(new_node)
#             new_node.setNext(current)
#     def index(self, item):
#         current = self.head
#         pos = 0
#         found = False
#         while current is not None and not found:
#             if current.getData() is item:
#                 found = True
#             else:
#                 current = current.getNext()
#                 pos += 1
#         if found:
#             pass
#         else:
#             pos = None
#         return pos

#     def pop(self, position = None):
#         if position > self.size():
#             print ('Index out of bounds')
#             raise IndexError
#         current = self.head
#         if position is None:
#             ret = current.getData()
#             self.head = current.getNext()
#         else:
#             pos = 0
#             previous = None
#             while pos < position:
#                 previous = current
#                 current = current.getNext()
#                 pos += 1
#                 ret = current.getData()
#             previous.setNext(current.getNext())
#         print (ret)
#         return ret
#     def append(self, item):
#         current = self.head
#         previous = None
#         pos = 0
#         length = self.size()
#         while pos < length:
#             previous = current
#             current = current.getNext()
#             pos += 1
#         new_node = Node(item)
#         if previous is None:
#             new_node.setNext(current)
#             self.head = new_node
#         else:
#             previous.setNext(new_node)
#     def printList(self):
#         current = self.head
#         while current is not None:
#             print (current.getData())
#             current = current.getNext()
# ll = LinkedList()
# ll.add('l')
# ll.add('H')
# ll.insert(1,'e')
# ll.append('l')
# ll.append('o')
# ll.printList()

# Chapter 25: Linked List Node

# Write a simple Linked List Node in python
# class Node:
#     def __init__(self, cargo=None, next=None):
#         self.car = cargo
#         self.cdr = next 
#     def __str__(self):
#         return str(self.car)
#     def display(lst):
#         if lst:
#             w("%s " % lst)
#             display(lst.cdr)
#         else:
#             w("nil\n")

# Chapter 26: Filter

# Basic use of filter

# names = ['Fred', 'Wilma', 'Barney']
# def long_name(name):
#     return len(name) > 5

# print(filter(long_name, names))
# # Out: ['Barney']
# print([name for name in names if len(name) > 5])


# print((name for name in names if len(name) > 5) )

# print(name for name in names if len(name) > 5) 

# Filter without function

# list(filter(None, [1, 0, 2, [], '', 'a'])) 

# print([i for i in [1, 0, 2, [], '', 'a'] if i])

# print((i for i in [1, 0, 2, [], '', 'a'] if i) )

# Filter as short-circuit check

# car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
# def find_something_smaller_than(name_value_tuple):
#     print('Check {0}, {1}$'.format(*name_value_tuple))
#     return name_value_tuple[1] < 100
# next(filter(find_something_smaller_than, car_shop))

# Complementary function: filterfalse, ifilterfalse

# from itertools import filterfalse
# print(list(filterfalse(None, [1, 0, 2, [], '', 'a'])))

# names = ['Fred', 'Wilma', 'Barney']
# def long_name(name):
#  return len(name) > 5
# print(list(filterfalse(long_name, names)))

# car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
# def find_something_smaller_than(name_value_tuple):
#     print('Check {0}, {1}$'.format(*name_value_tuple))
#     return name_value_tuple[1] < 100
# print(next(filterfalse(find_something_smaller_than, car_shop)))


# car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
# generator = (car for car in car_shop if not car[1] < 100)
# print(next(generator))


# Chapter 27: Heapq

# Largest and smallest items in a collection

# import heapq
# numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
# print(heapq.nlargest(4, numbers))

# print(heapq.nsmallest(4, numbers))

# people = [
#  {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
#  {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
#  {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
#  {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
#  {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
#  {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
# ]
# oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
# print(oldest)
# youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
# print(youngest)

#  Smallest item in a collection
# import heapq
# numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
# heapq.heapify(numbers)
# print(numbers)

# heapq.heappop(numbers) # 2
# print(numbers)

# heapq.heappop(numbers) 
# print(numbers)


# Chapter 28: Tuple

#  Tuple

# t = tuple('lupins')
# print(t) # ('l', 'u', 'p', 'i', 'n', 's')
# t = tuple(range(3))
# print(t) 

#Tuples are immutable

# tuple1 = ('a', 'b', 'c', 'd', 'e')
# tuple2 = ('1','2','3')

# tuple3 = ('a', 'b', 'c', 'd', 'e')
# print(len(tuple1))
# print(max(tuple1))
# print(min(tuple1))
# list = [1,2,3,4,5]
# print(tuple(list))
# print(tuple1 + tuple2)

# Indexing Tuples
# x = (1, 2, 3)
# print(x[0] )
# print(x[1]) 
# print(x[2] )

# print(x[-1])
# print(x[-2]) 
# print(x[-3]) 
# print(x[:-1]) 
# print(x[-1:])
# print(x[1:3])

# : Reversing Elements
# colors = "red", "green", "blue"
# rev = colors[::-1]
# # rev: ("blue", "green", "red")
# colors = rev
# colors: ("blue", "green", "red")

#Chapter 29: Basic Input and Output

#Using the print function
# print("You can print \n escape characters too.")

#IUsing input() and raw_input()
# foo = input("Put a message here that asks the user for input: ")

#Function to prompt user for a number
# def input_number(msg, err_msg=None): 
#     while True:
#         try:
#             return float(input(msg))
#         except ValueError:
#             if err_msg is not None:
#                 print(err_msg)
# user_number = input_number("Enter a number: ")

#Printing a string without a newline at the end
# print("Hello, ", end="\n") 
# print("World!")

# print("Hello, ", end="") 
# print("World!")

# print("Hello, ", end="BREAK") 
# print("World!")

# import sys
# sys.stdout.write("Hello, ") 
# sys.stdout.write("World!")

#Chapter 31: os.path

#Join Paths
import os
# a = os.path.join('a', 'b', 'c')
# print(a)

#Path Component Manipulation
# p = os.path.join(os.getcwd(), 'foo.txt')
# print(p)
# print(os.path.dirname(p))
# print(os.path.basename(p))
# print(os.path.split(os.getcwd()))
# print(os.path.splitext(os.path.basename(p)))

#If the given path exists
# path = '/home/john/temp'
# print(os.path.exists(path))

# #check if the given path is a directory, file, symbolic link, mount point etc
# dirname = '/home/john/python'
# print(os.path.isdir(dirname))

# filename = dirname + 'main.py'
# print(os.path.isfile(filename))

# symlink = dirname + 'some_sym_link'
# print(os.path.islink(symlink))

# mount_path = '/home'
# print(os.path.ismount(mount_path))

#Absolute Path from Relative Path
# print(os.getcwd())
# print(os.path.abspath('foo'))
# print(os.path.abspath('../foo'))
# print(os.path.abspath('/foo'))

#Chapter 32: Iterables and Iterators

#Extract values one by one
# s = {1, 2}
# i = iter(s)
# a = next(i)
# print(a)
# b = next(i)
# print(b)
# c = next(i)
# print(c) #this will give you an error

# Iterating over entire iterable
# s = {1, 2, 3}
# for a in s:
#     print(a)
# l1 = list(s)

#Verify only one element in iterable
# a, = iterable 
# def foo():
#     yield 1
# a, = foo() 
# print(foo())
# nums = [1, 2, 3]
# print(a, nums)

#Chapter 33: Functions

#Defining and calling simple functions
# def greet(): 
#     print("Hello")
# greet()

# def greet_two(greeting): 
#     print(greeting)
# greet_two("hello")

# def greet_two(greeting="Howdy"): 
#     print(greeting)
# greet_two("true")

#Defining a function with an arbitrary number of arguments