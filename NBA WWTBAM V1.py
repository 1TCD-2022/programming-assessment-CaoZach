"""
Name: NBA WWTBAM
Author: Zach
Date: July 2022
Description: Who Wants to be a Millionaire comes to the NBA. Contestants
will answer many questions related to the NBA and progressively get
closer to winning the big million dollar jackpot
"""
import time

#initialise variables
easy_questions = ["What country does Luka Doncic come from? ","",""]
hard_questions = ["","",""]
money_counter = 0
valid_menu_choice = ["1","2"]


#print welcome message
print("""Hello! And welcome to Who Wants to Be a Millionaire: NBA Edition
You will be asked a series of questions. For each question you get correct
you'll progress closer and closer to the coveted million dollar jackpot!
""")
#ask the user for their name
username = input("Before we begin, can you tell me your name? ").strip()
print("Welcome to the show {}".format(username))
print("So {}, would you like to take on the easy or the hard set of questions? ".format(username))
user_set_choice = input("Type 1 for the easy questions and 2 for the hard questions ")
while not user_set_choice in valid_menu_choice:
    user_set_choice = input("Invalid Input, Type 1 for the easy questions and 2 for the hard questions ")
#If user inputs 1 use the easy set of questions    
if user_set_choice == "1":
    print("You chose the easy questions! Now for your first question, it should be an easy one: ")
    question_1 = print(easy_questions[0])
    #Wait 0.3 seconds before answering (will be longer in later iterations)
    time.sleep(0.3)
    print()
    print("a. Serbia")
    print("b. The Dallas Mavericks")
    print("c. Spain")
    print("d. USA")

#Repeat code until user answers a,b,c or d
user_answer = input("Enter a,b,c or d: ")
while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
    user_answer = input("Incorrect, please enter a,b,c or d: ")
if user_answer == "a":
    print("That's correct! Good job")
    #Add 100 dollars to the user's score
    money_counter += 100
    print("Well done! That moves you up to a total of {} dollars".format(money_counter))
elif user_answer == "b":
    print("I'm sorry that's incorrect")
elif user_answer == "c":
    print("I'm sorry that's incorrect")
elif user_answer == "d":
    print("I'm sorry that's incorrect")

