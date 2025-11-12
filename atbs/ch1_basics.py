# PYTHON BASICS

# REPL
print(2 + 2)
print(2)

# Order of Operations (Precedence)
print(2 + 3 + 6)
print((2 + 3) + 6)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print(2 + 2)
print(((5 - 1) * ((7 + 1) / (3 - 1))))

# SyntaxError: invalid syntax
# 5 + 
# 42 + 5 + * 2

# SyntaxError: unterminated string literal (detected at line 1)
# This error means you probably forgot the final single-quote character at the end of the string.

# String Concatenation + Replication
print('Alice' + 'Bob')

#Traceback (most recent call last):
#  File "<python-input-0>", line 1, in <module>
#    'Alice' + 42
#TypeError: can only concatenate str (not "int") to str

# Assignment Statements
spam = "Hello"
print(spam)
spam = "Goodbye"
print(spam)

# Variable Names
# It can’t have spaces.
# It can use only letters, numbers, and the underscore (_) character.
# It can’t begin with a number.
# It can’t be a Python keyword, such as if, for, return, or other keywords you’ll learn in this book.
# Table 1-3 shows examples of legal variable names.

# First Program
# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')