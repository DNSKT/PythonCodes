import random

print("Password Generator")
print("-----------------")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*()_+'

def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(alphabet + numbers + special + alphabet_upper)
    return password

while True:
    print(generate_password(10))
