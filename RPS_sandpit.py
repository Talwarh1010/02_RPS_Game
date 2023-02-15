
from ast import While
from urllib import response

def rounds():
    while True:
        error = "Please press <enter> or enter an integer more than 0"
        response = input("Choose between Rock(R), Paper(P), Scissors(S) or 000 to quit ")
        if response.isnumeric() == False:
            print(error)
        elif int(response) <= 0:
            print(error)
        else:
            break
final_round = rounds()

while True:
    round = 0
    if final_round == "":
        round += 1
        print(f'Continuous mode: Round #{round} ')
        if final_round == '000':
            break
    
        
    elif final_round == round - 1:
        break
    else:
        round += 1
        print(f'Round #{round} out of {final_round} has begun')
        

