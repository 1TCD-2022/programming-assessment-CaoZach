"""
Name: NBA WWTBAM V3
Author: Zach
Date: July 2022
Description: Who Wants to be a Millionaire comes to the NBA. Contestants
will answer many questions related to the NBA and progressively get
closer to winning the big million dollar jackpot
"""
import time

#initialise variables
questions = ["What country does Luka Doncic come from? ","What team won the 2022 NBA championship? ","What jersey number did Russell Westbrook wear in 2022? ",\
                  "Which city do the Nets play in? ","How many NBA championships did Michael Jordan win? ","What NBA team as of 2022 has missed the playoffs for 16 straight seasons? ",\
                  "Which NBA player’s nickname is “The Logo?” ","Who was the #3 NBA draft pick in 2003? ","Which NBA team did Kobe Bryant score 81 points against in 2006? ",\
             "How many points per game did Jaylen Brown average in the 2022 regular season? ","Which NBA player was suspended for 72 games following “The Malice at the Palace?”",\
             "What NBA team drafted Donovan Mitchell in 2017? ","What were the first NBA hoops made out of? ","Which NBA player was given the nickname “Baby Jordan?” ",\
             "Who was the first black player in the NBA? "]
money_tree = ["100","200","300","500","1000","2000","4000","8000","16000","32000",\
                 "64000","125000","250000","500000","1000000"]
valid_menu_choice = ["1","2"]
money_counter = money_tree [0]
game_over = False



#print welcome message
print("""Hello! And welcome to Who Wants to Be a Millionaire: NBA Edition
You will be asked a series of questions. For each question you get correct
you'll progress closer and closer to the coveted million dollar jackpot!
""")
#ask the user for their name
username = input("Before we begin, can you tell me your name? ").strip()
print("Welcome to the show {}".format(username))
print("So {}, would you like to play Millionaire today? ".format(username))
user_set_choice = input("Type 1 to play and 2 to walk away ")
while not user_set_choice in valid_menu_choice:
    user_set_choice = input("Invalid Input, Type 1 for the easy questions and 2 for the hard questions ")
#If user inputs 1 use the easy set of questions    
if user_set_choice == "1":
    print("Now for your first question, it should be an easy one: ")
    question_1 = print(questions[0])
    #Wait 0.3 seconds before displaying answers
    time.sleep(0.3)
    print()
    print("a. Slovenia")
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
        #Add 100 dollars to the user's score taking the value from the money tree list
        money_counter = money_tree[0]
        print("Well done! That moves you up to a total of {} dollars".format(money_counter))
        #Introduce the next question using this block of code as the other answers would end the game
        print("Now on to the next question")
        question_2 = print(questions[1])
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
            #Update the users score to 200 using the value from the money tree
            money_counter = money_tree[1]
            print("Well done! That moves you up to a total of {} dollars".format(money_counter))
            print("Now on to the next question")
            question_3 = print(questions[2])
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
                print("You answered b...")
                time.sleep(0.3)
                print("That's correct! Good job")
                #Update users score
                money_counter = money_tree[2]
                print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                print("Now on to the next question")
                question_4 = print(questions[3])
                time.sleep(0.3) 
                print()
                print("a. Brooklyn")
                print("b. New York City")
                print("c. Madrid")
                print("d. Los Angeles")

                user_answer = input("Enter a,b,c or d: ").lower()
                while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                    user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
                if user_answer == "a":
                    print("You answered a...")
                    time.sleep(0.3)
                    print("That's correct! Good job")
                    money_counter = money_tree[3]
                    print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                    print("Now on to the next question")
                    question_5 = print(questions[4])
                    time.sleep(0.3) 
                    print()
                    print("a. 4")
                    print("b. 6")
                    print("c. 3")
                    print("d. 5")

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
                        print("That's correct! Good job")
                        money_counter = money_tree[4]
                        print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                        print("Now on to the next question")
                        question_6 = print(questions[5])
                        time.sleep(0.3) 
                        print()
                        print("a. The Brooklyn Nets")
                        print("b. The Minnesota Timberwolves")
                        print("c. The Detroit Pistons")
                        print("d. The Sacramento Kings")

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
                            money_counter = money_tree[5]
                            print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                            print("Now on to the next question")
                            question_7 = print(questions[6])
                            time.sleep(0.3) 
                            print()
                            print("a. Wilt Chamberlain")
                            print("b. Kobe Bryant")
                            print("c. Jerry West")
                            print("d. Michael Jordan")

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
                                print("That's correct! Good job")
                                money_counter = money_tree[6]
                                print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                print("Now on to the next question")
                                question_8 = print(questions[7])
                                time.sleep(0.3) 
                                print()
                                print("a. Lebron James")
                                print("b. Chris Bosh")
                                print("c. Dwyane Wade")
                                print("d. Carmelo Anthony")

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
                                    money_counter = money_tree[7]
                                    print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                    print("Now on to the next question")
                                    question_9 = print(questions[8])
                                    time.sleep(0.3) 
                                    print()
                                    print("a. The Toronto Raptors")
                                    print("b. The Golden State Warriors")
                                    print("c. The Dallas Mavericks")
                                    print("d. The Kansas City Chiefs")

                                    user_answer = input("Enter a,b,c or d: ").lower()
                                    while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                                        user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
                                    if user_answer == "a":
                                        print("You answered a...")
                                        time.sleep(0.3)
                                        print("That's correct! Good job")
                                        money_counter = money_tree[8]
                                        print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                        print("Now on to the next question")
                                        question_10 = print(questions[9])
                                        time.sleep(0.3) 
                                        print()
                                        print("a. 24.2")
                                        print("b. 25.5")
                                        print("c. 30.4")
                                        print("d. 23.6")

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
                                            money_counter = money_tree[9]
                                            print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                            print("Now on to the next question")
                                            question_11 = print(questions[10])
                                            time.sleep(0.3) 
                                            print()
                                            print("a. Ben Wallace")
                                            print("b. Ron Artest")
                                            print("c. Kobe Bryant")
                                            print("d. Reggie Miller")

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
                                                print("That's correct! Good job")
                                                money_counter = money_tree[10]
                                                print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                                print("Now on to the next question")
                                                question_12 = print(questions[11])
                                                time.sleep(0.3) 
                                                print()
                                                print("a. The Denver Nuggets")
                                                print("b. The Utah Jazz")
                                                print("c. The New York Knicks")
                                                print("d. The Chicago Bulls")

                                                user_answer = input("Enter a,b,c or d: ").lower()
                                                while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                                                    user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
                                                if user_answer == "a":
                                                    print("You answered a...")
                                                    time.sleep(0.3)
                                                    print("That's correct! Good job")
                                                    money_counter = money_tree[11]
                                                    print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                                    print("Now on to the next question")
                                                    question_13 = print(questions[12])
                                                    time.sleep(0.3) 
                                                    print()
                                                    print("a. Milk Crates")
                                                    print("b. Cardboard Boxes")
                                                    print("c. Peach Baskets")
                                                    print("d. Rubbish Bins")

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
                                                        print("That's correct! Good job")
                                                        money_counter = money_tree[12]
                                                        print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                                        print("Now on to the next question")
                                                        question_14 = print(questions[13])
                                                        time.sleep(0.3) 
                                                        print()
                                                        print("a. Harold Miner")
                                                        print("b. Lebron James")
                                                        print("c. Andrew Wiggins")
                                                        print("d. Kobe Bryant")

                                                        user_answer = input("Enter a,b,c or d: ").lower()
                                                        while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                                                            user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
                                                        if user_answer == "a":
                                                            print("You answered a...")
                                                            time.sleep(0.3)
                                                            print("That's correct! Good job")
                                                            money_counter = money_tree[13]
                                                            print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                                            print("Now on to the final question")
                                                            print("{}, you have the chance to win a million dollars!".format(username))
                                                            question_15 = print(questions[14])
                                                            time.sleep(0.3) 
                                                            print()
                                                            print("a. Wilt Chamberlain")
                                                            print("b. Bill Russell")
                                                            print("c. Julius Erving")
                                                            print("d. Earl Lloyd")

                                                            user_answer = input("Enter a,b,c or d: ").lower()
                                                            while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                                                                user_answer = input("Incorrect, please enter a,b,c or d: ").lower()
                                                            if user_answer == "a":
                                                                print("You answered a...")
                                                                #change the time sleep to 2 seconds as it is the final question
                                                                time.sleep(2)
                                                                print("I'm sorry that's incorrect. Unfortunately your run ends here.")
                                                                game_over == True
                                                            elif user_answer == "b":
                                                                print("You answered b...")
                                                                time.sleep(2)
                                                                print("I'm sorry that's incorrect. Unfortunately your run ends here.")
                                                                game_over == True
                                                            elif user_answer == "c":
                                                                print("You answered c...")
                                                                time.sleep(2)
                                                                print("I'm sorry that's incorrect. Unfortunately your run ends here.")
                                                                game_over == True
                                                            elif user_answer == "d":
                                                                print("You answered d...")
                                                                time.sleep(2)
                                                                #Print winning message
                                                                print("That's correct! Good job")
                                                                money_counter = money_tree[14]
                                                                print("Well done! That moves you up to a total of {} dollars".format(money_counter))
                                                                print("You did it {}, you're a millionaire!".format(username))

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

                            elif user_answer == "d":
                                print("You answered d...")
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
#Implement safety nets so if user has passed either 1000 or 32000 they keep those amounts respectively
if money_counter >= money_tree[9]:
    money_counter = money_tree [9]
    print("Well {}, luckily you managed to pass a safety net".format(username))
    print("That means you have earned a total of {} dollars".format(money_counter))
elif money_counter >= money_tree[4]:
    money_counter = money_tree[4]
    print("Well {}, luckily you managed to pass a safety net".format(username))
    print("That means you have earned a total of {} dollars".format(money_counter))
else:
    print("Unfortunately you didn't pass any safety nets. So you didn't earn any money.")
print("Thank you for playing {} it was a pleasure to have you on the show.".format(username))

