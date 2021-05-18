import random
list = [1,2,3,4,5,6]
while True:
    print("--------------------------------")
    print("-------Hand Cricket Game--------")
    print("--------------------------------")
    user = 0
    computer = 0
    user_sum = 0
    computer_sum = 0
    print("1. Choose Batting \n2. Choose Fielding")
    user_choice = int(input("Pick any one option above: "))
    if user_choice == 1:
        print("User chooses batting\nComputer chooses fielding")
        computer_choice = 0
        while user_choice != computer_choice:
            computer_choice = random.choice(list)
            print("Computer selects ",computer_choice)
            user_choice = random.choice(list)
            print("User selects ",user_choice)
            if (user_choice == 1) or (user_choice == 2) or (user_choice == 3) or (user_choice == 4) or (user_choice == 5) or (user_choice == 6):
                user_sum = user_sum + user_choice
                if user_choice == computer_choice:
                    user_sum = user_sum - user_choice
        print("Howzaaaaaaaaaat!! Score of the user is: ",user_sum)
        print("Target to Computer is: ",user_sum+1)
        computer_choice = 0
        while computer_choice != user_choice:
            computer_choice = random.choice(list)
            print("Computer selects ",computer_choice)
            user_choice = random.choice(list)
            print("User selects ",user_choice)
            if (computer_choice == 1) or (computer_choice == 2) or (computer_choice == 3) or (computer_choice == 4) or (computer_choice == 5) or (computer_choice == 6):
                computer_sum = computer_sum + computer_choice
                if computer_choice == user_choice:
                    computer_sum = computer_sum - computer_choice
        print("Howzaaaaaaaaaat!! Score of the computer is: ",computer_sum)
        if user_sum < computer_sum:
            print("*****Computer Wins*****")
        else:
            print("*****User Wins*****")
    elif user_choice == 2:
        print("User chooses fielding\nComputer chooses batting")
        computer_choice = 0
        while computer_choice != user_choice:
            computer_choice = random.choice(list)
            print("Computer selects ",computer_choice)
            user_choice = random.choice(list)
            print("User selects ",user_choice)
            if (computer_choice == 1) or (computer_choice == 2) or (computer_choice == 3) or (computer_choice == 4) or (computer_choice == 5) or (computer_choice == 6):
                computer_sum = computer_sum + computer_choice
                if computer_choice == user_choice:
                    computer_sum = computer_sum - computer_choice
        print("Howzaaaaaaaaaat!! Score of the computer is: ",computer_sum)
        print("Target to User is: ",computer_sum+1)
        user_choice = 0
        while user_choice != computer_choice:
            computer_choice = random.choice(list)
            print("Computer selects ",computer_choice)
            user_choice = random.choice(list)
            print("User selects ",user_choice)
            if (user_choice == 1) or (user_choice == 2) or (user_choice == 3) or (user_choice == 4) or (user_choice == 5) or (user_choice == 6):
                user_sum = user_sum + user_choice
                if user_choice == computer_choice:
                    user_sum = user_sum - user_choice
        print("Howzaaaaaaaaaat!! Score of the user is: ",user_sum)
        if user_sum < computer_sum:
            print("*****Computer Wins*****")
        else:
            print("*****User Wins*****")
    else:
        print("Invalid Choice")
    n = input("\nDo you want to play again?(Yes/Exit)\n")
    if n == "Yes":
        continue
    else:
        break