def compare(computer, chosen):
    computer_points = 0
    user_points = 0
    lost = "You lost"
    if computer == "rock" and chosen == "scissors":
        print(lost)
        computer_points += 1
        
    elif computer == "scissors" and chosen == "paper":
        print(lost)
        computer_points += 1
        
    elif computer == "paper" and chosen == "rock":
        print(lost)
        computer_points += 1
    else:
        print("You won")
        user_points += 1
        
    