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
import random
def playgame(name):
    """Generates random int and checks user input guess"""
    number =  random.randrange(1, 101)
    guesscount = 0
    while True:
        userinput = input(f"{name}, choose a number betwee 1 and 100\n")
        if validateinput(userinput) != False:
            useranswer = validateinput(userinput)
            guesscount += 1
            if number != useranswer:
                if number > useranswer:
                    print("Oh, no!")
                    print(f"Your number, {useranswer}, is too small")
                else:
                    print("Ee, gads!")
                    print(f"Your number, {useranswer}, is too large")
            else:
                print("Woohoo!")
                print(f"Well done, {name}! {useranswer} is the right answer!! You found my number in {guesscount} tries.")
                return(guesscount)
        else:
            print(f"That guess, {userinput} is not valid. Try again.")

def validateinput(userinput):
    """verifies if user input is an int within range (1-100)"""
    try:
        val = int(userinput)
        if val >= 1 and val < 101:
            return int(userinput)
        else:
            return False
    except ValueError:
        return False    
## using two ifs instead of try/except
    # if userinput.isdigit() == True:
    #     if int(userinput) >= 1 and int(userinput) < 101:
    #         return int(userinput)
    #     else:
    #         return False
    # else:
    #     return False


#create function that loops through playgame function
    #save guesscount variable from playgame function
    #variable to track the lowest guess thus far
    #ask if user wants to play again
        #if yes, call playgame function
def ask_playagain():
    reloopanswer = input("Type Y or N \n")
    if (reloopanswer != "Y") and (reloopanswer != "N"):
        print("Did not understand your answer-- Try again.")
        ask_playagain()
    else:
        return reloopanswer

def reloop():
    """Loops through game until user decides to stop playing. Keeps track of past scores."""
    guesslist = []
    print("Welcome to the guessing game!")
    name = input("What is your name?")
    while True:
        guesscount = playgame(name)
        guesslist.append(guesscount)
        bestscore = min(guesslist)
        print("Congrations on winning. Would you like to play again to improve your score?")
        print(f"Your current best score is {bestscore}.")
        if ask_playagain() == "N":
            return "Goodbye!"
                

print(reloop())