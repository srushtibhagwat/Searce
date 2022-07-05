#COMPARISON

#Comparison by `is` vs `==`

# a = 'Python is fun!'
# b = 'Python is fun!'
# print(a == b) 
# print(a is b)
# a = [1, 2, 3, 4, 5]
# b = a 
# print(a == b) 
# print(a is b)
# b = a[:] 
# print(a == b)
# print(a is b)

# a = 'short' 
# b = 'short' 
# c=5
# d=5
# print(a is b) 
# print(c is d)

# a = 'not so short'
# b = 'not so short'
# c = 1000
# d = 1000
# print(a is b) 
# print(c is d)

# if myvar is not None:
#     pass
# if myvar is None:
#     pass

# sentinel = object()
# def myfunc(var=sentinel):
#     if var is sentinel:
#         pass
#     else:
#         pass



#Greater than or less than

# print(12 > 4)
# print(12 < 4)
# print(1<4)

# print("alpha" < "beta")
# print("gamma" > "beta")
# print("gamma" < "OMEGA")
# print("GAMMA" < "OMEGA")


#Not equal to


# print(12 != 1)
# print(12 != '12')
# print('12' != '12')



#Equal To


# print(12 == 12)
# print(12 == 1)
# print('12' == '12')
# print('spam' == 'spam')
# print('spam' == 'spam')
# print('12' == 12)


#Comparing Objects


# class Foo(object):
#     def __init__(self, item):
#         self.my_item = item
#     def __eq__(self, other):
#         return self.my_item == other.my_item
# a = Foo(5)
# b = Foo(5)
# print(a == b)
# print(a != b)
# print(a is b)

# class Bar(object):
#     def __init__(self, item):
#         self.other_item = item
#     def __eq__(self, other):
#         return self.other_item == other.other_item
#     def __ne__(self, other):
#         return self.other_item != other.other_item

# c = Bar(5)
# print(a == c)



#LOOPS

#Break and Continue in Loops

#break statement

# i=0
# while i < 7:
#     print(i) 
#     if i == 4:
#         print("Breaking from loop")
#         break
#     i += 1
    
# for i in (0, 1, 2, 3, 4): 
#     print(i)
#     if i == 2: 
#         break

#continue statement


# for i in (0, 1, 2, 3, 4, 5):
#     if i == 2 or i == 4:
#         continue 
#     print(i)


#Nested Loops

# while True:
#     for i in range(1,5):
#         if i == 2:
#             break


#Use return from within a function as a break

# def break_all():
#     for j in range(1, 5):
#         for i in range(1,4):
#             if i*j == 6:
#                 return(i) 
#             print(i*j)

# def break_loop():
#     for i in range(1, 5):
#         if (i == 2): 
#             return(i)
#         print(i) 
#     return(5)



#For loops


# for i in [0, 1, 2, 3, 4]: 
#     print(i)



#Iterating over lists


# for x in ['one', 'two', 'three', 'four']: 
#     print(x)

# for x in range(1, 6): 
#     print(x)

# for index, item in enumerate(['one', 'two', 'three', 'four']): 
#     print(index, '::', item)

# x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
# print(x)



#Loops with an "else" clause



# for i in range(3):
#      print(i)
# else: 
#     print('done')



# i=0
# while i < 3: 
#     print(i)
#     i += 1 
# else:
#     print('done')


# for i in range(2): 
#     print(i)
#     if i == 1: 
#          break
#     else: 
#         print('done')


# a = [1, 2, 3, 4] 
# for i in a:
#     if type(i) is not int: 
#         print(i)
#         break 
#     else:
#         print("no exception")


#The Pass Statement


# for x in range(10):
#     pass 


#Iterating over dictionaries

#d = {"a": 1, "b": 2, "c": 3}

# for key in d: 
#     print(key)

# for key in d.keys():
#      print(key)

# for value in d.values(): 
#     print(value)

# for key, value in d.items(): 
#     print(key, "::", value)


#The "half loop" do-while


# a = 10 
# while True:
#     a = a-1 
#     print(a) 
#     if a<7:
#         break
# print('Done.')


# Looping and Unpacking


# collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
# for item in collection: 
#     i1 = item[0]
#     i2 = item[1] 
#     i3 = item[2]


# Iterating dierent portion of a list with dierent


lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
# for s in lst:
#     print(s[:1])

# for idx, s in enumerate(lst):
#     print("%s has an index of %d" % (s, idx))

# for i in range(2,4):
#     print("lst at %d contains %s" % (i, lst[i]))

# for s in lst[1::2]: 
#     print(s)
# for i in range(1, len(lst), 2): 
#     print(lst[i])



#While Loop


# i=0
# while i < 4:
#     #loop statements
#     i= i +1


# while True:
#     print("Infinite loop")




#ARRAYS



#Basic Introduction to Arrays

# from array import *
# my_array = array('i', [1,2,3,4,5]) print(my_array[1])
# #2
# print(my_array[2])
# #3
# print(my_array[0])

# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# for i in my_array:
#     print(i)


#Append any value to the array using append() method

# from array import *

# my_array = array('i', [1,2,3,4,5]) 
# my_array.append(6)
# for i in my_array:
#     print(i)


#Insert value in an array using insert() method

# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# my_array.insert(0,0)
# for i in my_array:
#      print(i)


#Extend python array using extend() method


# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# my_extnd_array = array('i', [7,8,9,10]) 
# my_array.extend(my_extnd_array)
# for i in my_array:
#     print(i)


#Add items from list into array using fromlist() method

# from array import *
# my_array = array('i', [1,2,3,4,5])
# c=[11,12,13]
# my_array.fromlist(c)
# for i in my_array:
#     print(i)



#Remove any array element using remove() method
# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# my_array.remove(4)
# for i in my_array:
#     print(i)


#Remove last array element using pop() method

# from array import *
# my_array = array('i', [1,2,3,4,5])
# my_array.pop()
# for i in my_array:
#     print(i)



#Fetch any element through its index using index() method
# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# print(my_array.index(5))
# my_array = array('i', [1,2,3,3,5]) 
# print(my_array.index(3))



#Reverse a python array using reverse() method
# from array import *
# my_array = array('i', [1,2,3,4,5])
# my_array.reverse()
# for i in my_array:
#     print(i)


#Get array buer information through buer_info() method
# from array import *
# my_array = array('i', [1,2,3,4,5])
# my_array.buffer_info()
# (33881712, 5)
# for i in my_array:
#     print(i)


#Check for number of occurrences of an element using count() method
# from array import *
# my_array = array('i', [1,2,3,3,5]) 
# print(my_array.count(3))


#Convert array to a python list with same elements using tolist() method

# from array import *
# my_array = array('i', [1,2,3,4,5]) 
# c = my_array.tolist()
# print(c)



#MULTIDIMENSIONAL ARRAY

# lst=[[1,2,3],[4,5,6],[7,8,9]]
# print (lst[0]) 
# print (lst[1]) 
# print (lst[2]) 

# print (lst[0][0]) 
# print (lst[0][1])

#Lists in lists in lists in..


# [[[111,112,113],[121,122,123],[131,132,133]],\
# [[211,212,213],[221,222,223],[231,232,233]],\
# [[311,312,313],[321,322,323],[331,332,333]]]

# print(myarray)
# print(myarray[1]) 
# print(myarray[2][1]) 
# print(myarray[1][0][2])


#DICTIONARY


#Avoiding KeyError Exceptions

# mydict = {}
# print(mydict)
# print(mydict.get("foo", "bar"))
# print(mydict)
# print(mydict.setdefault("foo", "bar")) 
# print(mydict)


#Iterating Over a Dictionary

#d = {'a': 1, 'b': 2, 'c':3} 
# for key in d:
#     print(key, d[key])

# for key, value in d.items(): 
#     print(key, value)


#Dictionary with default values


# from collections import defaultdict
# d = defaultdict(int)
# d['key']
# d['key'] = 5
# d['key']
# d = defaultdict(lambda: 'empty') 
# d['key']
# d['key'] = 'full'
# d['key']



#Merging dictionaries


# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
# fishdog = {**fish, **dog}
# print(fishdog)


#Accessing keys and values
# mydict = {'a': '1', 'b': '2' }
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())



#Accessing values of a dictionary


# dictionary = {"Hello": 1234, "World": 5678} 
# print(dictionary["Hello"])


#Creating an ordered dictionary


# from collections import OrderedDict
# d = OrderedDict()
# d['first'] = 1
# d['second'] = 2
# d['third'] = 3
# d['last'] = 4
# for key in d: print(key, d[key])


#Unpacking dictionaries using the ** operator


# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
# fishdog = {**fish, **dog}
# print(fishdog)


#The dict() constructor


# print(dict(a=1, b=2, c=3))
# print(dict([('d', 4), ('e', 5), ('f', 6)]))  
# print(dict([('a', 1)], b=2, c=3))
# print(dict({'a' : 1, 'b' : 2}, c=3))


#Dictionaries Example

# car = {}
# car["wheels"] = 4
# car["color"] = "Red"
# car["model"] = "Corvette"

# print("Little " + car["color"] + " " + car["model"] + "!")


#All combinations of dictionary values

# import itertools
# options = {
#     "x": ["a", "b"],
#     "y": [10, 20, 30]}
# keys = options.keys()
# values = (options[key] for key in keys)
# combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)] 
# print(combinations)



#LIST

#List methods and supported operators


a = [1, 2, 3, 4, 5]

# #APPEND
# a.append(6)
# a.append(7)
# a.append(7)
# print(a)

# b = [8, 9]
# a.append(b)
# print(a)


#extend

# a = [1, 2, 3, 4, 5, 6, 7, 7]
# b = [8, 9, 10]

# a.extend(b)

# a.extend(range(3))
# a = [1, 2, 3, 4, 5, 6] + [7, 7] + b



#index

# print(a.index(7))
# print(a.index(49))

#insert

# a.insert(0, 0) 

# a.remove(0)
# a.remove(9)
# a.reverse()
# a.sort()
# print(a)
# print(a.count(7))


#Accessing list values



lst = [1, 2, 3, 4] 
# print(lst[0]) 
# print(lst[1])
# print(lst[-1])
# print(lst[-2])
# print(lst[1:])
# print(lst[:3])
# print(lst[::2])
# print(lst[::-1])
# print(lst[-1:0:-1])
# print(lst[5:8])
# print(lst[1:10])

# data = 'chandan purohit 22 2000'
# name_slice = slice(0,19)
# age_slice = slice(19,21)
# salary_slice = slice(22,None)
# print(data[name_slice]) 
# print(data[age_slice]) 
# print(data[salary_slice])


#Checking if list is empty


# lst = []
# if not lst:
#     print("list is empty")


#Iterating over a list
# my_list = ['foo', 'bar', 'baz'] 
# # for item in my_list:
# #     print(item)


# for (index, item) in enumerate(my_list):
#     print('The item in position {} is: {}'.format(index, item))


#Checking whether an item is in a list


# lst = ['test', 'twest', 'tweast', 'treast']
# print('test' in lst)
# print('toast' in lst)


#Any and All



# nums = [1, 1, 0, 1] 
# print(all(nums))
# chars = ['a', 'b', 'c', 'd'] 
# print(all(chars))


# nums = [1, 1, 0, 1]
# print(any(nums))

# vals = [None, None, None, False] 
# print(any(vals))



#Concatenate and Merge lists


# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
# for a, b in zip(alist, blist):
#      print(a, b)


# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3', 'b4'] 
# for a, b in zip(alist, blist):
#     print(a, b)


# alist = [123, 'xyz', 'zara', 'abc'] 
# alist.insert(3, [2009]) 
# print("Final List :", alist)


#Length of a list



# print(len(['one', 'two']))
# print(len(['one', [2, 3], 'four']))



#Remove duplicate values in list


# names = ["aixk", "duke", "edik", "tofp", "duke"] 
# print(list(set(names)))


#Comparison of lists



# print([1, 10, 100] < [2, 10, 100])

# print([1, 10, 100] < [1, 10, 100])

# print([1, 10, 100] < [1, 10, 101]) 
# print([1, 10, 100] < [0, 10, 100]) 



#Accessing values in nested list



# alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
# print(alist[0][0][1])

# for row in alist: 
#     for col in row:
#         print(col)



#Initializing a List to a Fixed Number of Elements


# my_list=[{1}] * 10
# print(my_list)
# [{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}]
# my_list[0].add(2)
# print(my_list)


#LIST COMPREHENSION


#List Comprehensions


# squares = [x * x for x in (1, 2, 3, 4)]
# print(squares)

#Conditional List Comprehensions

# even_numbers = []
# for x in range(10): 
#     if x % 2 == 0:
#         even_numbers.append(x)
#     print(even_numbers)


# numbers = []
# for x in range(10):
#     if x % 2 == 0: 
#         temp = x
#     else:        
#         temp = -1
#     numbers.append(2 * temp + 1) 
# print(numbers)



#Dictionary Comprehensions


# dict1 = {'w': 1, 'x': 1}
# dict2 = {'x': 2, 'y': 2, 'z': 2}
# {k: v for d in [dict1, dict2] for k, v in d.items()}



#List Comprehensions with Nested Loops



# data = [[1, 2], [3, 4], [5, 6]] 
# output = []
# for each_list in data:
#     for element in each_list:   
#         output.append(element)
# print(output)


# data = [[1, 2], [3, 4], [5, 6]]
# output = [element for each_list in data for element in each_list] 
# print(output)


# data = [[1], [2, 3], [4, 5]]
# output = [element for each_list in data

# if len(each_list) == 2 
# for element in each_list 
# if element != 5]
# print(output)


#Iterate two or more list simultaneously within list comprehension


# list_1 = [1, 2, 3 , 4]
# list_2 = ['a', 'b', 'c', 'd']
# list_3 = ['6', '7', '8', '9']
# [(i, j) for i, j in zip(list_1, list_2)]


#LIST SLICING


#Using the third "step" argument



# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(lst[::2])

# print(lst[::3])


#Selecting a sublist from a list


# lst = ['a', 'b', 'c', 'd', 'e']
# print(lst[2:4])


# print(lst[:4])


#Reversing a list with slicing



# a = [1, 2, 3, 4, 5]

# b = a[::-1]

# a.reverse() 

# if a == b:
#     print(True) 
# print(b)


