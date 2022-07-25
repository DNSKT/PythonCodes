from random import randint as ri

def inp(text):
    return int(input(text))

attemps = 0

n = ri(1, 100)
guess = inp('¿Qué número estoy pensando? \n[>] ')
while True:
    if guess < n:
        guess = inp('¡Más! ')
        attemps += 1
    elif guess > n:
        guess = inp('¡Menos! ')
        attemps += 1
    else:
        print('\t¡Acertaste!')
        print('\t¡Tu puntuación es de: ', attemps)
        break
print('\n\tEl número era', n)

