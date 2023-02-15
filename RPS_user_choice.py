def user_choice(question, error , valid):
    loop = True
    while loop == True:
            response = input(question).lower()
            for item  in valid:
                if response  == item or response == item[0]:
                    return item
            else:
                print(error)
            
user = ""
while user != 'xxx':
    valid = ['rock', 'paper', 'scissors', '000']
    user = user_choice(" Choose Rock / Paper / Scissors, R / P / S  or 000 to quit: ","Please enter rock, paper or scissors", valid )
    print()
    print(f"You chose {user}")
    print()
            