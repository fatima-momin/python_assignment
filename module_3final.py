
print("QUESTION : 4 Write a Python function to get the largest number, smallest num and sum of all from a list.")
mylist = []
number = int(input('How many elements enter in List: '))
for n in range(number):
    element = int(input('Enter element '))
    mylist.append(element)
print("Largest element in the list is :", max(mylist))
print("Smallest element in the list is :", min(mylist))




print("QUESTION : 6 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.")
def similar_words(words):
  character = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      character += 1
  return character

print(similar_words(['abc', 'aba', 'abc', '1221']))

print("QUESTION : 7  Write a Python program to remove duplicates from a list")
A = [10,20,30,20,10,50,60,40,80,50,40]

duplicate_items = set()
unique_items = []
for x in A:
    if x not in duplicate_items:
        unique_items.append(x)
        duplicate_items.add(x)

print(duplicate_items)

print("QUESTION : 8 Write a Python program to check a list is empty or not.")
list1 = [45,55]
if (list1):
    print("The list is not empty")
else:
    print("Empty List")


print("QUESTION : 9 Write a Python function that takes two lists and returns true if they have at least one common member. ")
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

print("QUESTION : 10  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30")
def values():
    l=list()
    for i in range(1,30):
        l.append(i**2)
    print(l)
values()

print("QUESTION : 11  Write a Python function that takes a list and returns a new list with unique elements of the first list.")
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 




print("QUESTION : 12 Write a Python program to convert a list of characters into a string.")
s = ['H','E','L','L','O']
string = ''.join(s)
print(string)

print("QUESTION : 13 Write a Python program to select an item randomly from a list")
import random
fruits = ['Apple','Kiwi','Mango','Watermelon','Papaya','Grapes']
print(random.choice(fruits))


print("QUESTION : 14 Write a Python program to find the second smallest number in a list.")
number = [6,3,4,5,6,0,4]
print(f"number:{number}")

first_num=10000
second_numm=10000
for i in number:
    if number<first_num :
         second_numm = first_num
    elif number > first_num and number<second_numm:
        second_numm = number

print(f"first_num:{first_num}")
print(f"second_numm:{second_numm}")


print("QUESTION : 15 Write a Python program to get unique values from a list ")
unique_list = [1,15,16,'BHOOMI','HELLO',78,15]
print(set(unique_list))


print("QUESTION : 16 Write a Python program to check whether a list contains a sub list")
mylist = [15,20,25,30,35,['x',23,56]]
for   i in mylist:
    if len(i) > 1:
        print("sublist is present in list")
    else:
        print("sublist is not present in list")


print("QUESTION : 17 Write a Python program to split a list into different variables. ")
names = ['bhoomi','shital','mayur']
print("names:",names)
a,b,c = names
print("var a:",a)
print("var b:",b)
print("var c:",c)


print("QUESTION : 19 Write a Python program to create a tuple with different data types")
tuple = ("bhoomi","hello",3.2,True,15)
print(tuple)


print("QUESTION : 20 Write a Python program to create a tuple with numbers. ")
tuple = 5, 10, 15, 20, 25
print(tuple)

tuplex = 5,
print(tuple)



print("QUESTION : 21 Write a Python program to convert a tuple to a string.")
tuple_string = ('h','e','l','l','o')
string = ''.join(tuple_string)
print(string)

print("QUESTION : 22 Write a Python program to check whether an element exists within a tuple. ")
tuple = ("B",8,"H","S")
print("B" in tuple)
print(7 in tuple)

print("QUESTION : 23 Write a Python program to find the length of a tuple.")
tuple_length = ("BHOOMI")
print(tuple_length)
print(len(tuple_length))

print("QUESTION : 24 Write a Python program to convert a list to a tuple. ")
mylist = ['BHOOMI','SHITAL','NIYATI','KRUPA','RUTU']
print(mylist)

tuple_list = tuple(mylist)
print(tuple_list)

print("QUESTION : 25 Write a Python program to reverse a tuple. ")
x = (input("enter your name:"))
y= reversed(x)

print(tuple(y))


print("QUESTION : 26 Write a Python program to replace last value of tuples in a list")
l = [(10,20,30),(40,50,60),(70,80,90)]
print([t[:-1] + (100,) for t in l])



print("QUESTION : 27 Write a Python program to find the repeated items of a tuple ")
tuple_repeated = (2,4,6,6,7,5,2,7)
print(tuple_repeated)
count = tuple.count(4)
print(count)

print("QUESTION : 28 Write a Python program to remove an empty tuple(s) from a list of tuples. ")
list1 = [(1,4,6,7),(4,5),()]
for tuple in list1:
    if (len(tuple)==0):
        list1.remove(tuple)
print(list1)



print("QUESTION : 29 Write a Python program to unzip a list of tuples into individual lists.")
l = [(1,5), (3,4), (7,5)]
print(list(zip(*l)))


print("QUESTION : 30 Write a Python program to convert a list of tuples into a dictionary.")
def dicto(x):
    return(dict(x))
x=[("BHOOMI",20),("SHITAL",25)]
print(dicto(x))


print("QUESTION : 32 Write a Python script to sort (ascending and descending) a dictionary by value. ")
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)


print("QUESTION : 34 Write a Python script to check if a given key already exists in a dictionary. ")
d = {1:10,2:20,3:10,5:50}
def is_key_present(x):
    if x in d:
        print("Key present in the dictionary")
    else:
        print("Key is not present in the dictionary")
        is_key_present(10)
        


print("QUESTION : 37 Write a Python script to print a dictionary where the keys are numbers between 1 and 15.")
d = dict()
for i in range(1,16):
    d[i]=i**2
print(d)



print("QUESTION : 38 Write a Python program to check multiple keys exists in a dictionary ")
student = {
    'class' : 'v'
    
}
print(student.keys() >= {'class','name'})

print("QUESTION : 39  Write a Python script to merge two Python dictionaries ")
d1 = {'a':100,'b':200}
d2 = {'p':300,'q':400}

d = d1.copy()
d.update(d2)

print(d)



print("QUESTION : 40 Write a Python program to map two lists into a dictionary")
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)





print("QUESTION : 41 Write a Python program to combine two dictionary adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}")
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


print("QUESTION : 42 Write a Python program to print all unique values in a dictionary. ")
unique_list = [1,15,16,'BHOOMI','HELLO',78,15]
print(set(unique_list))


print("QUESTION : 46 Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] ")
dict1 = {"name": "abc"}
dict2 = {"email":"abc@gmail.com"}
combine = dict()
for dict in (dict1, dict2):
    for key, value in dict.items():
        combine[key] = value

print(combine)

print("QUESTION : 47 Write a Python program to create a dictionary from a string. ")
str1 = 'tops'
my_dict ={}
for letter in str1:
    my_dict[letter] = my_dict.get(letter,0)+ 1

print(my_dict)

print("QUESTION : 48 Write a Python function to calculate the factorial of a number (a nonnegative integer)")
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 

print("QUESTION : 49 Write a Python function to check whether a number is in a given range")


print("QUESTION : 50 Write a Python function to check whether a number is perfect or not. ")
num = int(input("enter your nunber:"))
sum = 0
for i in range (1,num):
    if num % i == 0:
        sum = sum +i
    if sum == num :
        print(num,'is a perfact number')
    else : 
        print(num,'is a not perfact number')



print("QUESTION : 51 Write a Python function that checks whether a passed string is palindrome or not ")
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('abca')) 



print("QUESTION : 58 Write a Python program to read a random line from a file. ")
import random
fruits = ['Apple','Kiwi','Mango','Watermelon','Papaya','Grapes']
print(random.choice(fruits))

print("QUESTION : 59 Write a Python program to convert degree to radian ")
import math
a =30 
rad = math.radians(a)
print("radians:",rad)

print("QUESTION : 60 Write a Python program to calculate the area of a trapezoid")
A = int(input("Enter the first base:"))
B = int(input("Enter the second base:"))
C = int(input("Enter the height:"))
Area = C * (A+B)/2
print('Area of Trapezoid is :',Area)


print("QUESTION : 61 Write a Python program to calculate the area of a parallelogram ")
b = int(input("enter your breath:"))
h = int(input("enter your height:"))

 
area = b * h
print("Area of parallelogram is :"+str(area))


print("QUESTION : 62 Write a Python program to calculate surface volume and area of a cylinder ")
pi = 22/7
h = float(input("Enter height of cylinder:"))
r = float(input("Enter radius of cylinder:"))
volume = pi * r * r * h
surfacearea = ((2*pi*r)*h) + ((pi*r**2)*2)
print('Volume is :',volume)
print('Surface area is : ',surfacearea)

print("QUESTION : 63 Write a Python program to returns sum of all divisors of a number ")
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(5))
print(sum_div(12))


"""

                            |MODULE-3 THEORY QUESTION|
-------------------------------------------------------------------------------------------
QUESTION : 1 What is List? How will you reverse a list? ")
ANS:
>>  Python knows a number of compound data types, used to group together 
other values. 

>>  The most versatile is the list, which can be written as a list of commaseparated values (items) between square brackets. 
Lists might contain items of different types, but usually the items all have the 
same type.

>>  Example : fruits = ['apples', 'oranges', 'pears', 'apricots']
    Example :fruits = ['apples', 1, 'pears', 2]

>>  In Python, there is a built-in function called reverse() that is used to reverse the list. 

>>  This is a simple and quick way to reverse a list that requires little memory. 

>>  SYNTAX: list_name.reverse()

>>  IMPLEMETNATION : 
    Reverse_list=[1,2,3,4,5]
    Reverse_list.reverse()
    print(Reverse_list)



QUESTION : 2 How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]
ANS: 
>>  Python provide a provision for slicing the lists using the subscript operators. 

>>  For slicing a list, one needs to provide the starting and ending index  in the subscript operator.

>>  list[start:end]



QUESTION : 3 Differentiate between append () and extend () methods? 
ANS : 
>>  Python append() method adds an element to a list, and the extend() method concatenates the first list with another list (or another iterable).
When append() method adds its argument as a single element to the end of a list, the length of the list itself will increase by one.
Whereas extend() method iterates over its argument adding each element to the list, extending the list.
The length of the list will increase by however many elements were in the iterable argument.



QUESTION : 18 What is tuple? Difference between list and tuple. 
ANS: 
>>  A tuple is a sequence of immutable Python objects. 

>>  Tuples are sequences, just like lists.

>>  The differences between tuples and lists are:

>>  The tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

>>  Example : fruits=(“Mango”,”Banana”,”Oranges”,23,44)
          numbers=(11,22,33,44)
          fruits=”Mango”,”Banana”,”Oranges”



QUESTION : 31  How will you create a dictionary using tuples in python? 
ANS: 
>>  Use dict() to convert a tuple to a dictionarty

>>  call dict(x) with x as the syntax (a,b) for (b,a) in tuple to create a dictionary
with key as the second elements in the tuple and values as the first elements in the tuple.



QUESTION : 35 How Do You Traverse Through A Dictionary Object In Python?
ANS:
>>  Dictionary in python an unordered collection of data values,used to store data values,
used to store data values like a map,unlike other data types that hold only a single value 
as an element,Dictionary holds the key: value pair.



QUESTION : 36 How Do You Check The Presence Of A Key In A Dictionary?
ANS: 
>>  To check, if a value exists in a dictionary, if a dictionary has contains a value, use the in operator and the 
values() method. use notin no check  if a value does not exists in a dictionary.


QUESTION : 43 Why Do You Use the Zip () Method in Python?
ANS:
>>  Python's zip() function creates an iterator that will aggregrate elements from  two or more iterables.
you can use the resulting iterator to quickly and consistently solve common programming problemss,
like creating dictionaries.


QUESTION : 52 How Many Basic Types Of Functions Are Available In Python?")
ANS:
>> There are two basic types of functions :
        1] Built in function : built in function are part of the python language ; for instance dir,len, or abs

        2] User defined function: user defined function are functions created with def keyword.



QUESTION : 53 How can you pick a random item from a list or tuple? 
ANS:
>>  Select randomly n ellements from a list using choice()

>>  The choice() method is used to return number for given sequence.

>>  The sequence can be a list or a tuple.

>>  This returns a single value from available data that considers duplicate values in the sequence(list)



QUESTION : 54 How can you pick a random item from a range? 
ANS: 


QUESTION : 55 How can you get a random number in python? 
ANS:
>>  To , generate random number in python, randint() function  is defined in random 
module.



QUESTION : 56 How will you set the starting value in generating random numbers?
ANS: 
>>  The random number generator needs a number to start with(a seed value),to be able to generate
a random number.

>> By default the random number generator uses the current system time. Use the seed() methiod t
customize the start number of the random number generator.



QUESTION : 57 How will you randomizes the items of a list in place?
ANS:
>>  The suffle() method randomizes the items of a list in place.











"""





