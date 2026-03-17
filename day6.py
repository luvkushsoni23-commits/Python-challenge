#Typecasting - conversion of one data type to another data type
'''
the python doesn't know what is written in inverted commas either it is a number or string it will treate all as string.
'''
#some inbuilt typecasting functions are - 
#int() - converts string to integer
#float() - converts string to float
#str() - converts integer or float to string
#str() - converts integer or float to string
#ord() - converts a character to its ASCII value
#hex() - converts an integer to a hexadecimal string
#oct() - converts an integer to an octal string
#bin() - converts an integer to a binary string
#tuple() - converts a list to a tuple
#list() - converts a tuple to a list
#set() - converts a list or tuple to a set
#dict() - converts a list of key-value pairs to a dictionary
#eval() - evaluates a string as a Python expression and returns the result
a = "1"
b = "2"
print(a + b) # it will concatenate the two strings and give output as 12
print(int(a) + int(b)) # it will convert the strings to integers and give output
# Types of typecastingg-

#Implicit typecasting - it is done automatically by the python interpreter when it encounters an expression with different data types. The python interpreter will convert the lower data type to the higher data type to avoid data loss.
a = 1.3
b = 4
print(a + b)

#Explicit typecasting - it is done manually by the programmer using the inbuilt typecasting functions. The programmer can convert a data type to another data type using the inbuilt typecasting functions.
a = 1
b = "string"
print(str(a) + b)
