# RETO 06 EQUIPO 1
"""
->Karem Melissa Agudelo Ojeda
->Miguel vasquez
->Juan David González Carrasquilla
->Paola Alexandra Daza Lopez
->Carolina Bedoya Rodriguez
->Sandra María Restrepo Sánchez
"""
#[“MDT546”,” KFC456”, “RTE123”,” TFG345”,” FGH789”,” SDR789”,” LMJ567”,” BHJ789”, “TBT516”,” “ASF476”]
#[“MDT546”,” KFC456”] RETIRAR.
#[“TBT516”,” ASF476”] INGRESAR VEHICULOS GRANDES.

print("               BIENVENIDO AL PARQUEADERO    ")
from datetime import date
today = date.today()
print(" ")
print(" ________                                __      __      ___.    ")
print(" \______ \   ____ ______ ______         /  \    /  \ ____\_ |__  ")
print("  |    |  \_/ __ \ \____ \\____ \   ____ \   \/\/   // __ \| __ \ ")
print("  |    `   \  ___/|  |_> >  |_> > /___/  \        /\  ___/| \_\ \ ")
print(" /_______  /\___  >   __/|   __/          \__/\  /  \___  >___  /")
print("         \/     \/|__|   |__|                  \/       \/    \/ ")
print("  ")
print("            ──▄▄▐▀▀▀▀▀▀▀▀▀▀▀▌▄▄──")
print("            ─▄▄▄█▄▄▄▄▄▄▄▄▄▄▄█▄▄▄─")
print("            ─█▄█░░█▓█▓█▓█▓█░░█▄█▌")
print("            ─▓▓█▀███████████▀█▓▓──")
print("            ─▓▓▀▀───────────▀▀▓▓──")
print("")
print("")
print("              HOY ES", (today)) 
print(" ")

lista=[]
def principal():   
    opcion="1"
    while(opcion!="5"):
         print("                  MENU              ")
         print(" ")
         print("    SELECCIONE LA OPCIÓN QUE DESEE  ")
         print("------------------------------------------")
         print("1- Ingresar vehiculos")
         print("2- Mostrar listado de Vehiculos")
         print("3- Ingresar vehículo en lugar")   
         print("4- Retirar vehículo")
         print("5. Finalizar")
         #print("6- Finalizar")
         opcion=input()
         if(opcion=="1"):
            capturar()
         elif(opcion=="2"):
            mostrar()
         elif(opcion=="3"):
            ingresar()     
         elif(opcion=="4"):
            eliminar() 
         elif(opcion=="5"):
            finalizar()

         else:
            print("[✗]Escoja otra opción!..")

def capturar():
    global lista
    
    print("[?]Ingrese cuantos Vehiculos guardara en el parqueadero")
    n = int(input())
    if n >10 : 
       print("Ha superdo las 10 celdas!")
    else: 
      for i in range(0,n):   
          print("[?]Ingrese las placas de los vehículos", i) 
          placa = input()
          lista.insert(i,placa)

def ingresar():
    t = str(input('[?] Que tipo de vehiculo es: \n [!] P : pequeño \n [!] G : grande \n'))
    if t == 'P':
        print("[?]Ingrese la placa del vehículo: ")
        placa = input()
        print("[?]Ingrese la celda donde desea colocar su vehículo")
        indice=int(input())
        longitud=len(lista)
        if (indice>longitud or indice <0 or longitud ==10):
            print("[!]El índice debe estar entre 0 y la" , longitud)
        else: 
            lista.insert(indice,placa)
            longitud=len(lista)
            print("[!]La longitud de la lista es:" , longitud)
            print("[✓]Vehículo ingresado")
    elif t == 'G':
        print("[?]Ingrese la placa del vehículo: ")
        placa = input()
        print("[?]Ingrese la celda donde desea colocar su vehículo")
        indice=int(input())
        longitud=len(lista)
        if (indice>longitud or indice <8 or longitud ==10):
            print("[!]El índice debe estar entre 8 y la" , longitud)
        else: 
            lista.insert(indice,placa)
            longitud=len(lista)
            print("[!]La longitud de la lista es:" , longitud)
            print("[✓]Vehículo ingresado")        

def mostrar():
    print("[!]los vehículos ingresados son: " , lista)
  
def eliminar():
    print("[?]Ingrese la celda donde se encuentra el vehículo a eliminar: ")
    indice=int(input())
    longitud=len(lista)
    if (indice>longitud or indice <0 or longitud ==11):
        print("[!]El índice debe estar entre 0 y la" , longitud)
    else: 
     del lista[indice]
     print("[✓]Vehículo retirado")
     

def finalizar():
    print("[!] FINALIZADO!...")
principal()
