def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

ed=input("Do you want to encrypt or decrypt? (e/d): ").lower()
if ed == 'e':
    string=input("Enter the string to encrypt: ")
    shift=int(input("Enter the shift value (1-25): "))
    encrypted_text = encrypt(string, shift)
    print(encrypted_text)
elif ed == 'd':
    string=input("Enter the string to decrypt: ")
    shift=int(input("Enter the shift value (1-25): "))
    decrypted_text = decrypt(string, shift)
    print(decrypted_text)
string=input("Enter the string to encrypt: ")
shift=int(input("Enter the shift value (1-25): "))
encrypted_text = encrypt(string, shift)
print(encrypted_text )