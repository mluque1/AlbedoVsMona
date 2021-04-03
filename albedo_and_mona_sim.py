import random

INIT_RECIPES = 1000
ATTEMPTS = 5000

def get_lucky(prob):
    return 1 if random.randrange(100) < prob else 0

def can_craft(mat):
    return mat > 3

def estimate_average(avg):
    return avg/ATTEMPTS

def ultimatum(name, avg):
    print(f'{name} obtains on average {estimate_average(avg)} materials with {INIT_RECIPES} initial recipes.')


if __name__ == '__main__':
    random.seed()

    #Albedo
    average = 0.0
    for i in range(ATTEMPTS):
        total = 0
        for j in range (INIT_RECIPES):
            total += 1
            total += get_lucky(10)
        average += total
    ultimatum('Albedo', average)


    #Mona
    average = 0.0
    for i in range (ATTEMPTS):
        total = 0
        materials = INIT_RECIPES * 3
        while can_craft(materials):
            materials -= 3
            total +=1
            materials += get_lucky(25)
        average += total
    ultimatum('Mona', average)
