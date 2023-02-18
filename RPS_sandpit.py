import random
def rounds():
    
    while True:
        error = "Please press <enter> or enter an integer more than 0"
        response = input("How many rounds do you want to play? ")
        if response == "":
                return response
        elif response.isdigit() and int(response) > 0 or response == "":
            return int(response)
            
        print(error)

def user_choice(question, error , valid):
    loop = True
    while loop == True:
            response = input(question).lower()
            for item  in valid:
                if response  == item or response == item[0]:
                    return item
            else:
                print(error)

def compare(computer1, chosen1):
    statement = ""
    while chosen1 != "000":
        if computer1 == "rock" and chosen1 == "scissors" or computer1 == "scissors" and chosen1 == "paper" or  computer1 == "paper" and chosen1 == "rock":
            statement = "You lost"
            
        elif computer1 == chosen1:
            statement = "Draw"
            
        else:
            statement = "You won"
            
        print(statement)
        
        return ""
    
# main routine
valid = ['rock', 'paper', 'scissors', '000']
final_round = rounds()
round_num = 0
while True:
    if final_round == "":
        round_num += 1
        heading = f'Continuous mode: Round #{round_num} '
    
    elif (round_num + 1) <= final_round:
        round_num += 1
        heading = 'Round #{} out of {} has begun'.format(round_num, final_round)
        print()
    
    else:
        break

    print(heading)
    chosen = user_choice(' Please choose Rock, paper, scissors or 000 to end : ', "Please enter rock, paper or scissors", valid)
    print()
    print(f'You chose {chosen}')
    print()
    computer = random.choice(valid[: -1])
    if chosen != "000":
        print(f"Computer choice : {computer}")
        print()
        compare(computer1 = computer, chosen1 = chosen)

    if chosen == "000":
        break


print("Thank you for playing")            