# 'x' in [1,2,3]

#'mykey' in {'mykey':345}

#d = {'mykey':345}
#345 in d.values()

#mylist = [10,20,30,40,50,100,1]
#min(mylist)
#max(mylist)

from random import shuffle

mylist = [2,3,4,62,3,323,45,67,32,76]
shuffle(mylist)
mylist

type(mylist)

from random import randint

randint(0,100)
#learning to save the random integer
saving_number = randint(0,100)

saving_number

# learning to use the input function
result = input('Enter a number: ')
result
type(result)
float(result)
int(result)