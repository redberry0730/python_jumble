import random

def ransomeware_attack(switch_condition):
    initial_dog = random.randint(1, 3)
    winning_dog = random.randint(1, 3)
    if switch_condition == True:
        if initial_dog != winning_dog:
            initial_dog = winning_dog
        elif initial_dog == winning_dog:
            initial_dog = False
    if initial_dog == winning_dog:
        return True

def simulator(total_trial, switch_condition):
    wins = 0
    for i in range(total_trial):
        if ransomeware_attack(switch_condition):
            wins += 1

    winning_chance = wins / total_trial
    print("Total trials:", total_trial)
    print("Switch:", switch_condition)
    print("Probability of winning:", winning_chance)

simulator(100000, True)
simulator(100000, False)



