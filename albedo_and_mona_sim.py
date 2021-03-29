import random

def get_lucky(prob):
    return 1 if random.randrange(100) < prob else 0

def can_craft():
    if materials > 3:
        return True
    return False

def estimate_average():
    return average/attempts

def ultimatum(name):
    print(f'{name} obtains on average {estimate_average()} materials with {initial_recipes} initial recipes.')


if __name__ == '__main__':
    initial_recipes = 1000 #Total number of initial recipes
    materials = initial_recipes * 3
    random.seed()
    attempts = 5000

    #Albedo
    average = 0.0
    for i in range(attempts):
        total = 0
        for j in range (initial_recipes):
            total += 1
            total += get_lucky(10)
        average += total
    ultimatum('Albedo')


    #Mona
    average = 0.0
    for i in range (attempts):
        total = 0
        materials = initial_recipes * 3
        while can_craft():
            materials -= 3
            total +=1
            materials += get_lucky(25)
        average += total
    ultimatum('Mona')
