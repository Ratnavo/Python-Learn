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

# FIND 33: Udemy Pierian Data

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

#### : Udemy Pierian Data : PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#   paper_doll('Hello') --> 'HHHeeellllllooo'
#    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = ''
    
    for char in text:
        result += char*3
    return result

#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#   blackjack(5,6,7) --> 18
#   blackjack(9,9,9) --> 'BUST'
#   blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    if sum([a,b,c]) <=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31: #here a,b,c are passed as list
        return sum([a,b,c])-10
    else:
        return "BUST"
    
    
#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
 
#   summer_69([1, 3, 5]) --> 9
#   summer_69([4, 5, 6, 7, 8, 9]) --> 9
#   summer_69([2, 1, 6, 9, 11]) --> 14

#nested for loop and while loop

def summer_69(arr):
    total = 0
    add = True
    
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
                
    return total