# reto 5
#MENÚ 
#Agregar pasajeros a la lista de viajeros.
#● Agregar ciudades a la lista de ciudades.
#● Dado el DNI (cédula) de un pasajero, ver a que ciudad viaja.
#● Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#● Dado el DNI (cédula) de un pasajero, ver a que país viaja.
#● Dado un país, mostrar cuántos pasajeros viajan a esa ciudad.
#● Salir del programa.

viajeros = []
ciudades = []

def agregar_viajeros(viajeros):
      nombre=input("[?] Nombre: ")
      while nombre != "f":
        cedula=input("[?] Cedula: ")
        destino=input("[?] Destino: ")
        viajeros.append((nombre,cedula,destino))
        print(viajeros)
        nombre=input("[?] Nombre: ")        
      return(viajeros)

def agregar_ciudades(ciudades):
      ciudad=input("[?] Ingrese el nombre de la ciudad: ")
      while ciudad != "f":
        pais=input("[?] Ingrese el nombre del pais: ")
        ciudades.append((ciudad,pais))
        print(ciudades)
        ciudad=input("[?] Ingrese el nombre de la ciudad: ")
      return(ciudad)

def cantidad_viajeros_ciudad(viajeros):
  cantidad = 0
  for viajeros in viajeros:
    if viajeros[2] == ciudad:
      cantidad += 1

def buscar_ciudad(viajero, cedula):
  for viajero in viajeros:
    if viajero[1] == cedula:
        return (viajero[2])

while True:
  print('1. Agregar pasajeros')
  print('2. Agregar ciudades')
  print('3. Buscar ciudad')
  print('4. Contar numero de pasajeros que viajan a la ciudad\n')
  opcion = int(input("[?] Ingrese una opcion: "))


  if  opcion == 1:
    viajero = agregar_viajeros(viajeros)

  elif opcion == 2:
    ciudad = agregar_ciudades(ciudades)

  elif opcion == 3:
    cedula = int(input("[?] Ingrese la cedula del pasajero: "))
    print("[!] El viajero viaja a: ",buscar_ciudad(viajero, cedula))
  
  elif opcion == 4:
    ciudad = input("[?] Ingrese el nombre de la ciudad: ")
    print("[!] La cantidad de pasajeros que viajan a la ciudad: ",cantidad_viajeros_ciudad(viajeros))

  else:
    print("[!] Opcion incorrecta")



