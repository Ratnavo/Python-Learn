from ensurepip import version


# Learning From Pierian Data
# Learning Methods
mylist = [1,2,3]
mylist.append(4)
print(mylist)

# Methods are built-in objects in Python
mylist.pop()
print(mylist)

#==================================================

# Learning how to use function
# def - Keyword telling Python this is a function
# def name_of_function():
#         "Docstring explain function"
# above statement "name_of_function" - known as snake casing where we use all lowercase with underscores between words.
# () stands for parenthesis which is used here at the end. Later on we can pass in arguments/parameters into the fucntion.
# Function can accept arguments to be passed by the user.
# return = this is a keyword that allows to use the output of a function to a new vairable.

#==================================================

# Basic function of python

def name_of_function():
    print("hello")
name_of_function()

def say_hello(name):
    print(f'Hello {name}')
say_hello('Ratnavo') 


# Function using return

def add_num(num1,num2):
    return num1+num2
result = add_num(2,2)    
print(result)

# Diff between print and return is that return saves the value.

def print_result(a,b):
    print(a+b)
savea = print_result(1,2)
print(savea)

def return_result(c,d):
    return c+d
return_result(10,12)
saveb = return_result(10,12)
print(saveb)
    
# Check data types