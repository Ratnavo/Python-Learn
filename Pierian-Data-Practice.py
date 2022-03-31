#Topic: 07 Statement Assessment
# Use range to print all the even numbers from 0 to 10
for num in range(0,11,2): #using step size
    print(num)

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
statements = 'Sam Print only the words that start with s in this sentence'
for letter in statements:
    if letter[0].lower() == 's':
        print(letter)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#Approach-1
list_new = [nums for nums in range(1,51) if nums%3==0]

#Approach-2 : If we are not saving the number in list
newlist = range(1,51)
for x in newlist:
    if x%3==0:
        print(x)


# Go through the string below and if the length of a word is even print "even!"
new_string = 'Print every word in this sentence that has an even number of letters'

for x in new_string.split():
    if len(x)%2==0:
        print(x+ " is even")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%3==0:
        print('Fizz')
    elif x%5==0:
        print('Buzz')
    else:
        print(x)

# Use List Comprehension to create a list of the first letters of every word in the string below:
string01 = 'Create a list of the first letters of every word in this string'
string02 = [x[0] for x in string01.split()]
print(string02)

#alternative of using list comprehension use append statement
mystring = 'hello' # We are creating a list from a string
newlist = []
for letter in mystring:
    newlist.append(letter)
print(newlist)

#Nested loop

newlist01 = []

for number_x in [2,4,6]:
    for number_y in [100,200,312]:
        newlist01.append(number_x*number_y)
        print(newlist01)