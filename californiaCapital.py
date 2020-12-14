"""

this program allows the user an input of up to 3 attempts to guess "What is the capial of California" answer = "Sacramento"

First set maxAttempts = 3, then create a loop to iterate 3 times. Each iteration = +1 counter to maxAttempts. if input = Sacramento, output would be "Correct!" and finish the loop 
if input != Sacramento +1 to counter up to 3 and output "Max allotted attempts have been used." Then print out "The correct answer was Sacramento."


"""
"""
main
    question = "What is the capital of California?"
    answer = California
    ask (question, answer)

ask
    tries = 0
    loop three times
        increment tries
        ask user input
        check to see if user input is equal to answer
            if so, print "Correct" then exit loop
    if not correct
        print to the user "You have used up your allotted attempts."
        print the correct answer "The Correct answer is Sacramento."

main

"""

def main():
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask (question, answer)

def ask(question, answer, max_Attempts=3):
    tries = 0
    ans = ""
    while tries < max_Attempts:
        tries = tries + 1 
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have exceeded you maximum number of attempts.")

main()