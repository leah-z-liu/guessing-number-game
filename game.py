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
def playGame():
    print("Welcome to the guessing game!")
    name = input("What is your name?")
    number =  random.randrange(1, 101)
    guesscount = 0
    #print (number)
    while True:
    #     useranswer = int(input(f"{name}, choose a number betwee 1 and 100\n"))
    # except:
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
                return(f"Well done, {name}! {useranswer} is the right answer!! You found my number in {guesscount} tries.")
        else:
            print(f"That guess, {userinput} is not valid. Try again.")

# def checknumber(userinput):
#     if number != useranswer:
#         if number > useranswer:
#             print("Oh, no!")
#             print(f"Your number, {useranswer}, is too small")
#         else:
#             print("Ee, gads!")
#             print(f"Your number, {useranswer}, is too large")
#     else:
#         print("Woohoo!")
#         return(f"Well done, {name}! {useranswer} is the right answer!! You found my number in {guesscount} tries.")

def validateinput(userinput):
    try:
        val = int(userinput)
        if val >= 1 and val < 101:
            return int(userinput)
        else:
            return False
    except ValueError:
        return False    
    # if userinput.isdigit() == True:
    #     if int(userinput) >= 1 and int(userinput) < 101:
    #         return int(userinput)
    #     else:
    #         return False
    # else:
    #     return False



print(playGame())
