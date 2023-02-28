import random


# Displays instructions for the user
def instructions():
    yes_no = user_choice("Have you played this game before? ", "Please enter yes or no", ['yes', 'no'])
    if yes_no == "no":
        print("""
        **** How to Play ****
        Choose either a number of rounds or press <enter> for Continuous mode
        Then for each round, choose from rock / paper / scissors or 000 to quit

        You can type r/p/s/0 if you do not want to type the entire word

        The rules are...
        Rock beats scissor
        Scissors beats paper
        Paper beats rock
        
        *** Have fun***"
            """)


# Validates the amount of rounds the user wants to play
def rounds():
    while True:
        error = "Please press <enter> or enter an integer more than 0"
        response = input("How many rounds do you want to play? ")
        if response == "":
            return response
        elif response.isdigit() and int(response) > 0 or response == "":
            return int(response)

        print(error)


# Validates the user's choice (R, P, S)
def user_choice(question, error, valid_list):
    while True:
        response = input(question).lower()
        for item in valid_list:
            if response == item or response == item[0]:
                return item
        else:
            print(error)
            print()


# main routine
print("Welcome to Rock, Paper, Scissors")

# Checks if the user has played the game before
instructions()
print()

final_round = rounds()
round_num = 0
win = 0
loss = 0
draw = 0
rounds_percentage = 0

# Checks the type of round, and the amount of rounds and displays round number
while True:
    if final_round == "":
        round_num += 1
        heading = f'Continuous mode: Round #{round_num} '
    elif (round_num + 1) <= final_round:
        round_num += 1
        heading = f'==== Round #{round_num} out of {final_round} has begun ===='
        print()


    else:
        round_num -= 1
        break

    print(heading)
    print()
    chosen = user_choice(' Please choose Rock, paper, scissors or 000 to end : ',
                         " Please enter rock, paper or scissors ", ['rock', 'paper', 'scissors', '000'])
    print()
    print(f'You chose {chosen}')

    # Compares the user's choice with computer's choice. Also tallies the result of the game
    computer = random.choice(['rock', 'paper', 'scissors', '000'][: -1])

    if chosen != "000":
        print(f"Computer choice : {computer}")
        print()

        if computer == "rock" and chosen == "scissors" or \
        computer == "scissors" and chosen == "paper" or computer == "paper" and chosen == "rock":
            
            statement = "❌❌You lost❌❌"
            loss += 1

        elif computer == chosen:
            statement = "🇹 🇹 You tied 🇹 🇹 "
            draw += 1

        else:
            statement = "✔️ ✔️ You won✔️ ✔️ "
            win += 1

        print(statement)

    if chosen == "000":
        round_num -= 1
        break

# Converts the score to percentages

win_percentage = round(win / round_num * 100, 2) if round_num != 0 else 0
draw_percentage = round(draw / round_num * 100, 2) if round_num != 0 else 0
loss_percentage = round(loss / round_num * 100, 2) if round_num != 0 else 0

# Prints overall results and regards the user
print()
print(
f"Results: Win - {win} - Percentage - {win_percentage}% | Draw - {draw} - Percentage - {draw_percentage}% | Loss - {loss} - Percentage {loss_percentage}%")
print()
print("Thank you for playing")
