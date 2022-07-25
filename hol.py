# 3X +1 

def isprime(num):
    if num % 2 == 0:
        return True
    else: return False


print('[!] Problema matematico 3x +1')

x = int(input('[?] ingrese un numero: '))
loop = 0
while loop < 120:
    loop = loop +1
    #print(loop)
    isprime(x)

    if isprime(x) == True:
       x = x / 2
       print('[!] ', x)
       isprime(x)

    if isprime(x) == False:
       x = x * 3 + 1
       print('[!] ',x)
       isprime(x)

