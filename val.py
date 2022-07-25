import json
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def Validar(x):
  if ValLen(x) == False:
    return False
  if ValPos(x) == False : 
    return False
  if ValNum(x) == True :
    return False
  if ValLetra(x[0], x[-1]) == False :
    return False
  if ValCantidad(x, 'k') == False :
    return False
  if ValSignos(x) == False :
    return False
  if ValMas(x) == False :
    return False
  else:
    return True

def ValLen(x):
  if len(x) == 10 : return True
  else:
    return False

def ValPos(x):
  if x[5] == '@' : return True
  else: return False

def ValNum(x):
  if bool(re.search(r'\d', x)) == True : return True
  else: return False

def ValLetra(x, z):
  if x != z: return True
  else : return False

def ValCantidad(x,z):
  if x.count(z) <= 3 : return True
  else : return False

def ValSignos(x):
  if '?' in x: return True
  if '=' in x: return True
  if '&' in x: return True
  else : return False

def ValMas(x):
  if '+' in x: return True
  else : return False

def ValJ():
  ValJson = open('CDIA.json')
  data = json.load(ValJson)

  for i in data['cdia']:
    print(i)

  ValJson.close()

def ValCheck(x):
    ValidarJson = open("CDIA.json", 'r')
    data = json.load(ValidarJson)
    for i in data['CDIA']:
        if x == i:
            return True
        else:
            return False

cdia = open('CDIA.json', 'r')
data = json.load(cdia)

def Check(x):
    for i in data['CDIA']:
        if x == i['name']:
            return True
    return False


m = {}
m['CDIA'] = []
m['CDIA'].append({
  'name' : 'Pablo',
  'cdia': 'XB&DE@E+TY'
})
m['CDIA'].append({
  'name' : 'Elena',
  'cdia': 'KB?D+@EHTY'
})
m['CDIA'].append({
  'name' : 'Pedro',
  'cdia': 'AB?DE@E+TY'
})
def dios(x,z):
  m['CDIA'].append({
    'name' : x,
    'cdia': z
  })
  with open('CDIA.json', 'w') as file:
    json.dump(m, file, indent=4)

def Valcalcular(x, m, l):
  h = l + 2
  fecha_nacimiento = datetime.strptime(x, "%d/%m/%Y")
  edad = relativedelta(datetime.now(), fecha_nacimiento)
  print(f"[!] {edad.years} años, {edad.months} meses y {edad.days} días")
  if edad.years > 12:
    print('[!] Proceso de nivel y mundo...')
    if 13 <= edad.years <=16 and m == 'No':
      print('[!] Seras enviado al nivel 2')
      print('[!] Tu nuevo mundo sera el 1')
    elif 13 <= edad.years <=16 and m == 'Si':
      print('[!] Seras enviado a tu nivel anterior', l)
      if l < 50:
        print('[!] Tu nuevo mundo sera el 2')
      elif l >= 50:
        print('[!] Tu nuevo mundo sera el 3')
    elif 17 <= edad.years <=40 and m == 'No':
      print('[!] Tu nuevo mundo sera el 4')
      print('[!] Seras enviado al nivel 1')
    elif 17 <= edad.years <=40 and m == 'Si':
      if l < 50:
        print('[!] Tu nuevo mundo sera el 5')
      elif l >= 50:
        print('[!] Tu nuevo mundo sera el 5')
      print('[!] Seras enviado a un nuevo nivel', h)
  
    return True
  elif edad.years < 12: 
    return False


#ab?de@e+ty
#(‘?’,’=’,’&’)
#ak?kk@x+ty