#Different variants can be used such as
    #->Snake,Water,gun
    #->Bomb,Tower,gun etc.
import random
list = ["Rock", "Paper", "Scissors"]
while True:
    print("****Rock Paper Scissors Game****")
    user = 0
    computer = 0
    for i in range(1,6):
        print("Round",i,"Start")
        print("1. ROCK \n2. PAPER \n3. SCISSORS")
        user_choice = int(input("Pick any one option above: "))
        if user_choice == 1:
            print("User selects Rock")
            user_choice = "Rock"
        elif user_choice == 2:
            print("User selects Paper")
            user_choice = "Paper"
        elif user_choice == 3:
            print("User selects Scissors")
            user_choice = "Scissors"
        else:
            print("Invalid Choice")
            break
        Computer_choice = random.choice(list)
        print("Computer selects ",Computer_choice)
        if user_choice == Computer_choice:
            print("The round is Drawn!! And no points gained")
        elif (user_choice == "Paper" and Computer_choice == "Rock") or (user_choice == "Scissors" and Computer_choice == "Paper") or (user_choice == "Rock" and Computer_choice == "Scissors"):
            user = user + 1
            print("Hurray! User wins this round")
        else:
            computer = computer + 1
            print("Computer wins this round")
    if user > computer:
        print("Congratulations! User wins the match")
        print("***SCORE***")
        print("User's Score: ",user,"Computer's Score: ",computer)
    elif computer > user:        
        print("User loses! Computer wins the match")
        print("***SCORE***")
        print("User's Score: ",user,"Computer's Score: ",computer)
    else:
        print("Match Drawn")
        print("User's Score: ",user,"Computer's Score: ",computer)
    n = input("Do you want to play again?(Yes/Exit)\n")
    if n == "Yes":
        continue
    else:
        break