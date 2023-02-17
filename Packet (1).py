from urllib.request import urlopen, Request
URL = input("URL: ")
Packet = input("Packet: ")

while True is True:
    P = Packet.encode()
    Data = urlopen(URL,P).read().decode()

ServerReturns = "Server Returning "+ str(Data)
print("Enviado!")