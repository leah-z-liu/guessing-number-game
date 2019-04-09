"""A number-guessing game."""

# Put your code here

# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player

def playGame():
    print("Welcome to the guessing game!")
    name = input("What is your name?")
    import random
    number =  random.randrange(1, 101)
    guesscount = 0
    #print (number)
    while True:
        useranswer = int(input("{}, choose a number betwee 1 and 100\n".format(name)))
        guesscount += 1
        #print(answer)
        if number != useranswer:
            if number > useranswer:
                print("Oh, no!")
                print("Your number, {}, is too small".format(useranswer))
            else:
                print("Ee, gads!")
                print("Your number, {}, is too large".format(useranswer))
        else:
            print("Woohoo!")
            return("Well done, {}! {} is the right answer!! You found my number in {} tries.".format(name, useranswer, guesscount))
            #break
print(playGame())
