from operator import truediv


print("QUESTION : 1 Write a Python program to check if a number is positive, negative or zero")
psum = 0
nsum = 0
num = float(input("enter your number:"))
if num>=0:
    print("positive number")
elif num==0:
    print("zero")
else:
    print("negative number")


print("QUESTION : 2 Write a Python program to get the Factorial number of given number.")
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


print("QUESTION : 3 Write a Python program to get the Fibonacci series of given range.")
num = int(input("enter your number:"))
x = 0
y = 1
z = 0
while (z<=num):
    print(z)
    x=y
    y=z
    z=x+y
   


print("QUESTION : 6.Write python program that swap two number with temp variable and without temp variable.")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print('Old value of num1 is {0} and num2 is {1}'.format(num1,num2))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print('new values of num1 is {0} and num2 is {1}'.format(num1,num2))



print("QUESTION : 7.Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.")
num = int(input("enter your number:"))
if num%2==0:
    print("even number")
else:
    print('odd number')



print("QUESTION : 8.Write a Python program to test whether a passed letter is a vowel or not. ")
A = input("enter a alphabet:")
if A in ('a','e','i','o','u'):
    print("THIS LETTER IS VOWEL")
elif A== 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("THIS LETTER IS NOT VOWEL")



print("QUESTION : 9 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
ans = num1 + num2 + num3
print("ans = ",ans)



print("QUESTION : 10.Write a Python program that will return true if the two give integer values are equal or their sum or difference is 5.")
def test_number5(x,y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False
print(test_number5(7,2))
print(test_number5(3,2))
print(test_number5(3,2))
print(test_number5(7,3))
print(test_number5(27,56))

print("QUESTION : 11.Write a python program to sum of the first n positive integers.")
num = int(input("input a number:"))
sum_num = (num * (num+1))/2
print("Sum of the first",num,"positive integer:",sum_num)




print("QUESTION : 12 Write a Python program to calculate the length of a string.")
str = input("Enter a string: ")
print("Length of the input string is:", len(str))




print("QUESTION : 13.Write a Python program to count the number of characters (character frequency) in a string.")
string = (input("enter your string:"))
s = {}
for i in string:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)




print("QUESTION : 15 Write a Python program to count occurrences of a substring in a string.")
str = 'python programming'
print()
print(str.count("python"))
print()


print("QUESTION : 16 Write a Python program to count the occurrences of each word in a given sentence")
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts








print("QUESTION : 17 Write a Python program to get a single string from two given strings, separated by a. space and swap the first two characters of each string.")
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))




print("QUESTION : 18 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged")
def add_string(string1):
    length = len(string1)

    if length > 2:
        if string1[-3:] == 'ing':
            string1 += 'ly'
        else:
            string1 += 'ing'
        return string1
print(add_string('ab'))
print(add_string('abcing'))
print(add_string('stringly'))





print("QUESTION : 19 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.")
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)],'good')
        return str1
    else:
        return str1
print(not_poor('the lyrics is not that poor!'))
print(not_poor('the lyrics is poor!'))


print("QUESTION : 20 Write a Python function that takes a list of words and returns the length of the longest one.")
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][0,word_len[-1][1]]
result = find_longest_word(["HEY","Hiii"])
print("\nLongest word:",[1])
print("\nLongest of the longest word:",result[0])





print("QUESTION : 21 Write a Python function to reverses a string if its length is a multiple of 4.")
name = input("enter your name:")
if(len(name)%4==0):
    print(name[::-1])
else:
    print("can't")




print("QUESTION : 22 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty str.")
def string_both_ends(str):
    if len(str) <2:
        return ''

    return str[0:2] +  str[-2]

print(string_both_ends('python'))
print(string_both_ends)




print("QUESTION : 23 Write a Python function to insert a string in the middle of a string.")
def insert_string_middle(str,word):
    return str[:2] + word + str[2:]

print(insert_string_middle('[[]]','python'))



















