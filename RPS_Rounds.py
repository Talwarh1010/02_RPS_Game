from ast import While


def rounds():
    
    while True:
        error = "Please press <enter> or enter an integer more than 0"
        response = input("How many rounds do you want to play? ")
        if response.isdigit() and int(response) > 0:
            return int(response)
            
        print(error)
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
    chosen = input(' Please choose Rock, paper, scissors or 000 to end : ')
    if chosen == "000":
        break


print("Thank you for playing")