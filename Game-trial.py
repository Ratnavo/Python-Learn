#Three cup Monte

cup_shuffle = ['','0','']
from random import shuffle
shuffle(cup_shuffle)

def shuffle_list(cup_shuffle):
    shuffle(cup_shuffle)
    return cup_shuffle

# Take input from player
def player_guess():
    guess = ""
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2 ")
    return int(guess)

# Check the input list from player
def check_guess(cup_shuffle,guess):
    if cup_shuffle[guess] == '0':
        print('Correct!')
    else:
        print("Wrong guess.")
        print(cup_shuffle)
cup_shuffle = ['','0',''] # initial list
mixeditup = shuffle_list(cup_shuffle) #shuffle list
guess = player_guess() #user guess
check_guess(mixeditup,guess)