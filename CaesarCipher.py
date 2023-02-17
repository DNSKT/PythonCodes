chars = [
   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '
]

print('-----------------')
print('The Caesar Cipher')
print('-----------------')

def encode(text, shift):
    text = text.upper()
    encodedText = ''
    for char in text:
        charIndex = chars.index(char)
        newIndex = (charIndex + shift)
        newIndex = newIndex % len(chars)
        encodedText += chars[newIndex]
    return encodedText

def decode(encodedText, shift):
    encodedText = encodedText.upper()
    decodedText = ''
    for char in encodedText:
        charIndex = chars.index(char)
        newIndex = (charIndex - shift)
        newIndex = newIndex % len(chars)
        decodedText += chars[newIndex]
    return decodedText


text = input('[?] Enter a text: ')
shift = int(input('[?] Enter a shift: '))

menu = int(input('\n1. Encode\n2. Decode\n3. Exit\n'))

if menu == 1:
    print('[!] Encoded text: ',encode(text, shift))
elif menu == 2:
    print('[!] Decoded text: ', decode(text, shift))
elif menu == 3:
    print('Bye!')