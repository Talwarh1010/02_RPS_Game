def instructions(question):
    yes_no = input(question).lower()
    while True:
        if yes_no == "yes" or yes_no == "y":
            print("**** How to Play ****")
            print("Choose either a number of rounds or press <enter> for Continuous mode")
            print("Then for each round, choose from rock")
            print('/ paper / scissors or xxx to quit')
            print('You can type r/p/s/x if you')
            print("don't want to type the entire word.")
            print("The rules are...)")
            print(" Rock beats scissor")
            print("Scissors beats paper")
            print("Paper beats rock")
            print("*** Have fun***")
            break
        elif yes_no == "no" or yes_no == "n":
            break
        else:
            print(" Please enter yes or no ")
            
        
