import random
def instructions(question):
    
    while True:
        yes_no = input(question).lower()
        if yes_no == "no" or yes_no == "n":
            print("**** How to Play ****")
            print("Choose either a number of rounds or press <enter> for Continuous mode")
            print()
            print("Then for each round, choose from rock / paper / scissors or 000 to quit")
            print()
            print('You can type r/p/s/0 if you do not want to type the entire word  ')
            print()
            print("The rules are...)")
            print()
            print("Rock beats scissor")
            print()
            print("Scissors beats paper")
            print()
            print("Paper beats rock")
            print()
            print("*** Have fun***")
            print()
            break
        elif yes_no == "yes" or yes_no == "y":
            break
        else:
            print(" Please enter yes or no ")
            
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
                print()

def compare(computer1, chosen1):
    global win, loss, draw
    statement = ""
    while chosen1 != "000":
        if computer1 == "rock" and chosen1 == "scissors" or computer1 == "scissors" and chosen1 == "paper" or  computer1 == "paper" and chosen1 == "rock":
            statement = "❌❌You lost❌❌"
            loss += 1
            
        elif computer1 == chosen1:
            statement = "🇹 🇹 You tied 🇹 🇹 "
            draw += 1
            
        else:
            statement = "✔️ ✔️ You won✔️ ✔️ "
            win += 1
            
        print(statement)
        
        return win, loss, draw
    
# main routine
print("Welcome to Rock, Paper, Scissors")
print()
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
instructions("Have you played this game before? ")
print()
valid = ['rock', 'paper', 'scissors', '000']
final_round = rounds()
round_num = 0
win = 0
loss = 0
draw = 0
while True:
    if final_round == "":
        round_num += 1
        heading = f'Continuous mode: Round #{round_num} '
    
    elif (round_num + 1) <= final_round:
        round_num += 1
        heading = '==== Round #{} out of {} has begun ===='.format(round_num, final_round)
        print()
    
    else:
        break

    print(heading)
    print()
    chosen = user_choice(' Please choose Rock, paper, scissors or 000 to end : ', " Please enter rock, paper or scissors ", valid)
    print()
    print(f'You chose {chosen}')
    
    computer = random.choice(valid[: -1])
    if chosen != "000":
        print(f"Computer choice : {computer}")
        print()
        compare(computer1 = computer, chosen1 = chosen)
        

    if chosen == "000":
        break
win_percentage = win / round_num * 100
loss_percentage =   loss / round_num * 100
draw_percentage = draw / round_num * 100
print()
print(f"Results: Win - {win} - Percentage - {win_percentage}% | Draw - {draw} - Percentage - {draw_percentage}% | Loss - {loss} - Percentage {loss_percentage}%")
print()
print("Thank you for playing")            