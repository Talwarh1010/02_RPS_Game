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
    
    else:
        break
    print(heading)
    chosen = user_choice(' Please choose Rock, paper, scissors or 000 to end : ', "Please enter rock, paper or scissors", valid)
    print()
    print(f'You chose {chosen}')
    print()
    if chosen == "000":
        break


print("Thank you for playing")            
