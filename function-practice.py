#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#    lesser_of_two_evens(2,4) --> 2
#    lesser_of_two_evens(2,5) --> 5

from pkg_resources import working_set


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0: #checking both numbers are even
        if a < b:
            result = a
        else:
            result = b
    else:
        #one or both numbers are odd
        if a > b:
            result = a
        else:
            result = b
    return result

#OR
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0: #checking both numbers are even
        return min(a,b)
    else:
        return max(a,b)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)
    
    firstword = wordlist[0]
    secondword = wordlist[1]
    
    return firstword[0] == secondword [0]

# Check
animal_crackers('Levelheaded Llama')
# Check
animal_crackers('Crazy Kangaroo')

#OR

def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    
    return wordlist[0][0] == wordlist[1][0]
# Check
animal_crackers('Levelheaded Llama')
# Check
animal_crackers('Crazy Kangaroo')

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

#OR

def makes_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

# FIND 33: 

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

 #   has_33([1, 3, 3]) → True
 #   has_33([1, 3, 1, 3]) → False
 #   has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(0,len(nums)-1):
       if nums [i] ==3 and nums[i+1] == 3:
        return True
    else:
        return False