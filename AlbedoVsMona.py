import random
n = 10000
materiales = n * 3
input()

random.seed()
#Albedo

promedio = 0.0
repeticiones = 50000

for i in range(repeticiones):
    total = 0
    for j in range (n):
        total += 1
        if random.randrange(100) < 10 : total+=1
    promedio += total
promedio = promedio / repeticiones

print (f'Con {materiales} materiales Albedo obtiene en promedio: {promedio}')


#Mona
input()
random.seed()

promedio = 0.0
for i in range (repeticiones):
    total = 0
    materiales = n * 3
    while materiales >= 3:
        materiales -= 3
        total +=1
        if random.randrange(100) < 25 : materiales+=1
    promedio += total
promedio = promedio / repeticiones
materiales = n * 3
print (f'Con {materiales} materiales Mona obtiene en promedio: {promedio}')
