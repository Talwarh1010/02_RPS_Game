import random

def computer():
    valid = ['rock', 'paper', 'scissors', "000"]
    for item in range(1, 20):
        choice = random.choice(valid[: -1])
        print(choice, end ="\t")
        
computer()
    