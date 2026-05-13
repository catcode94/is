# OUTPUT:
# Enter the message: Mayank
# Enter the shift value (integer): 5
# Encrypted: Rfdfsp
# Decrypted: Mayank

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# User input
text_input = input("Enter the message: ")
try:
    shift_input = int(input("Enter the shift value (integer): "))

    encrypted_text = caesar_cipher(text_input, shift_input, mode='encrypt')
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = caesar_cipher(encrypted_text, shift_input, mode='decrypt')
    print(f"Decrypted: {decrypted_text}")
except ValueError:
    print("Error: Shift value must be an integer.")
