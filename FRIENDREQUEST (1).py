import requests

def ola(x):
    url = "http://gmdpseditor.7m.pl/database/uploadFriendRequest20.php"
    data = "gameVersion=21&binaryVersion=35&gdw=0&accountID=2740&gjp=AwMHBgIHAQUDBwY=&sessionID=&toAccountID={}&comment=T3dP&secret=Wmfd2893gb7".format(x)
    data.encode()
    headers = {'Host':'gmdpseditor.7m.pl', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': ''.format(len(data))}
    response = requests.post(url, data=data, headers=headers)
    print(response.text)

for x in range(8800, 9000):
    ola(x)
