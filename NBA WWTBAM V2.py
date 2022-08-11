"""
Name: NBA WWTBAM V2
Author: Zach
Date: July 2022
Description: Who Wants to be a Millionaire comes to the NBA. Contestants
will answer many questions related to the NBA and progressively get
closer to winning the big million dollar jackpot
"""
import time

#initialise variables
easy_questions = ["What country does Luka Doncic come from? ","What team won the 2022 NBA championship? ","What jersey number does Russell Westbrook wear? "]
hard_questions = ["","",""]
money_counter = 0
valid_menu_choice = ["1","2"]
game_over = False


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
    #Wait 0.3 seconds before displaying answers
    time.sleep(0.3)
    print()
    print("a. Serbia")
    print("b. The Dallas Mavericks")
    print("c. Spain")
    print("d. USA")

#Repeat code until user answers a,b,c or d
user_answer = input("Enter a,b,c or d: ").lower()
while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
    user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
if user_answer == "a":
    #Wait 0.3 seconds before displaying answers (Will be 2 seconds in final iteration) 
    print("You answered a...")
    time.sleep(0.3)
    print("That's correct! Good job")
    #Add 100 dollars to the user's score
    money_counter += 100
    print("Well done! That moves you up to a total of {} dollars".format(money_counter))
    #Introduce the next question using this block of code as the other answers would end the game
    print("Now on to the next question")
    question_2 = print(easy_questions[1])
    time.sleep(0.3) 
    print()
    print("a. Real Madrid")
    print("b. The Phoenix Suns")
    print("c. Faze Clan")
    print("d. The Golden State Warriors")

    #Repeat code until user answers a,b,c or d
    user_answer = input("Enter a,b,c or d: ").lower()
    while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
        user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
    if user_answer == "a":
        print("You answered a...")
        time.sleep(0.3)
        print("I'm sorry that's incorrect. Unfortunately your run ends here.")
        game_over == True
    elif user_answer == "b":
        print("You answered b...")
        time.sleep(0.3)
        print("I'm sorry that's incorrect. Unfortunately your run ends here.")
        game_over == True
    elif user_answer == "c":
        print("You answered c...")
        time.sleep(0.3)
        print("I'm sorry that's incorrect. Unfortunately your run ends here.")
        game_over == True
    elif user_answer == "d":
        print("You answered d...")
        time.sleep(0.3)
        print("That's correct! Good job")
        #Add 100 dollars to the user's score (will probably format this money tree into a list for efficiency in later iterations)
        money_counter += 100
        print("Well done! That moves you up to a total of {} dollars".format(money_counter))
        print("Now on to the next question")
        question_3 = print(easy_questions[2])
        time.sleep(0.3) 
        print()
        print("a. 69")
        print("b. 0")
        print("c. 4")
        print("d. 23")

        user_answer = input("Enter a,b,c or d: ").lower()
        while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
            user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
        if user_answer == "a":
            print("You answered a...")
            time.sleep(0.3)
            print("I'm sorry that's incorrect. Unfortunately your run ends here.")
            game_over == True
        elif user_answer == "b":
            print("You answered d...")
            time.sleep(0.3)
            print("That's correct! Good job")
            #Add 100 dollars to the user's score (will probably format this money tree into a list for efficiency in later iterations)
            money_counter += 100
            print("Well done! That moves you up to a total of {} dollars".format(money_counter))
        elif user_answer == "c":
            print("You answered c...")
            time.sleep(0.3)
            print("I'm sorry that's incorrect. Unfortunately your run ends here.")
            game_over == True
        elif user_answer == "d":
            print("You answered d...")
            time.sleep(0.3)
            print("I'm sorry that's incorrect. Unfortunately your run ends here.")
            game_over == True

elif user_answer == "b":
    print("You answered b...")
    time.sleep(0.3)
    print("I'm sorry that's incorrect. Unfortunately your run ends here.")
    game_over == True
    #Game will end after any wrong answer
elif user_answer == "c":
    print("You answered c...")
    time.sleep(0.3)
    print("I'm sorry that's incorrect. Unfortunately your run ends here.")
    game_over == True
elif user_answer == "d":
    print("You answered d...")
    time.sleep(0.3)
    print("I'm sorry that's incorrect. Unfortunately your run ends here.")
    game_over == True

time.sleep(0.3)
print("Thank you for playing {} it was a pleasure to have you on the show.".format(username))

