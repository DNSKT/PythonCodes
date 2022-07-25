#Miguel Fernando Vasquez - Melissa Agudelo
import val
print('[!]= World Craft ASCII =[!]\n')

name = str(input('\n[?] Digite su nombre:\n[>] '))
if val.Check(name):
    print('[!] El usuario se encuentra registrado.')
else:
    print("[!] El Usuario no se encuentra registrado.")
    cdia = str(input('[?] Ingrese su CDIA.\n[>] '))
    cdia_up = cdia.upper()
    if val.Validar(cdia_up) == True:
        print('\n[!] Usted puede entrar...')
        val.dios(name, cdia_up)
        birthday = input('[?] Ingrese su fecha de nacimiento (DD/MM/AAAA):\n[>] ')
        #val.Valcalcular(birthday)
        alias = str(input('[?] Ingrese su alias de jugador\n[>] '))
        menu = str(input('[?] Ya habias jugado previamente? Si/No\n[>] '))
        #val.Valcalcular(birthday, menu, level)
        if menu == 'Si':
            level = int(input('[?] Hasta nivel llegaste? (1 - 100)\n[>] '))
            if val.Valcalcular(birthday, menu, level) == True:
                print('\n[!] Edad Correcta')
            else:
                print('[X] Edad incorrecta.')
        if menu == 'No':
            level = 0
            if val.Valcalcular(birthday, menu, level) == True:
                print('\n[!] Edad Correcta')
            else:
                print('[X] Edad incorrecta.')