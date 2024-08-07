import random
import string
reward = 100
balance = int(input("Please enter your bucget: "))
string.digits
loto_int = random.sample(range(10), 3)  
loto = [str(i) for i in loto_int]
random.shuffle(loto)
know_one = reward * 0.1
know_two = reward * 0.5
know_three = reward
new_account = balance - 15

if balance >= 15:
    combination = input("Welcome to first play. Please enter your three digit combination: ")
    user_combination = list(combination)
    print("Your combination:", user_combination)
    print("Loto combination:", loto)
    
    if user_combination[0] not in loto and user_combination[1] not in loto and user_combination[2] not in loto:
        print("You couldn't guess any digit and couldn't get any reward. ")
        print("Last balance: ",new_account )
        
    elif (user_combination[0] in loto and user_combination[1] not in loto and user_combination[2] not in loto) or \
         (user_combination[0] not in loto and user_combination[1] in loto and user_combination[2] not in loto) or \
         (user_combination[0] not in loto and user_combination[1] not in loto and user_combination[2] in loto):
        print("Congratulations, you just guess one digit and you can only get 10% (",know_one,") of total reward" ) 
        print("Last balance: ",new_account + know_one)
        
    elif (user_combination[0] in loto and user_combination[1] in loto and user_combination[2] not in loto) or \
         (user_combination[0] in loto and user_combination[1] not in loto and user_combination[2] in loto) or \
         (user_combination[0] not in loto and user_combination[1] in loto and user_combination[2] in loto):
        print("Congratulations, you guess two digit and you can only get 50% (",know_two,") of total reward")
        print("Last balance: ", new_account + know_two)
        
    elif user_combination[0] in loto and user_combination[1] in loto and user_combination[2] in loto:
        print("Congratulations, you guess all digit and you can get 100% (",know_three,") of total reward")
        print("Last balance: ",new_account + know_three)
    else:
        None
else:
    print("Your must have at least 15 tl for one play.")