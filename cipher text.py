alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
direction = input("type whether you want to encrypt or decrypt : ")
shift =int(input("enter shift number : "))
text = input("enter text which u want to change").lower()
def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)
encrypt(plain_text=text,shift_amount=shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
direction = input('''enter what you want to "encode" or "decode" : ''').lower()
def code():
    text = input("enter the text you want to change : ")
    shift =int(input("enter the shift number here : "))
    cipher =""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher += new_letter
    print(cipher)

def decode():
    text_d  = input("enter the text you want to decode : ")
    shift_d = int(input("enter the shift number here : "))
    cypher =""
    for decoding in text_d:
        position = alphabet.index(decoding)
        new_position = position - shift_d
        new_letter = alphabet[new_position]
        cypher += new_letter
    print(cypher)
if direction == "encode":
    code()
elif direction == "decode":
    decode()



