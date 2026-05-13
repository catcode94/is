"""=== PRODUCT CIPHER (Caesar + Row Transposition) ===

1. Encrypt
2. Decrypt
Enter choice (1 / 2 or Encrypt / Decrypt): 2
Enter message: CQEREO
Enter Caesar shift: 4
Enter transposition key: qwerty

===== DECRYPTION PROCESS =====
Step 1 - After Transposition Decryption :  QECERO
Step 2 - After Caesar Decryption :  MAYANK

Final Decrypted Message : MAYANK
================================
"""

# CAESAR CIPHER
def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) + shift - 65) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) + shift - 97) % 26 + 97)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ROW TRANSPOSITION
def encrypt_row_transposition(message, key):
    message = message.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)
    rows = (len(message) + cols - 1) // cols

    message += 'X' * (rows * cols - len(message))

    grid = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        grid.append(row)

    order = sorted(range(len(key)), key=lambda k: key[k])

    cipher = ""
    for col in order:
        for r in range(rows):
            cipher += grid[r][col]

    return cipher


def decrypt_row_transposition(cipher, key):
    cipher = cipher.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)
    rows = len(cipher) // cols

    grid = [['' for _ in range(cols)] for _ in range(rows)]

    order = sorted(range(len(key)), key=lambda k: key[k])

    index = 0
    for col in order:
        for r in range(rows):
            grid[r][col] = cipher[index]
            index += 1

    message = ""
    for r in range(rows):
        for c in range(cols):
            message += grid[r][c]

    return message.rstrip('X')


# PRODUCT CIPHER
def product_encrypt(message, shift, key):
    print("\n===== ENCRYPTION PROCESS =====")

    step1 = caesar_encrypt(message, shift)
    print("Step 1 - Caesar Cipher Output : ", step1)

    step2 = encrypt_row_transposition(step1, key)
    print("Step 2 - Row Transposition Output : ", step2)

    print("\nFinal Encrypted Message :", step2)
    print("================================")

    return step2


def product_decrypt(cipher, shift, key):
    print("\n===== DECRYPTION PROCESS =====")

    step1 = decrypt_row_transposition(cipher, key)
    print("Step 1 - After Transposition Decryption : ", step1)

    step2 = caesar_decrypt(step1, shift)
    print("Step 2 - After Caesar Decryption : ", step2)

    print("\nFinal Decrypted Message :", step2)
    print("================================")

    return step2


# MAIN PROGRAM
print("=== PRODUCT CIPHER (Caesar + Row Transposition) ===")

print("\n1. Encrypt")
print("2. Decrypt")

choice_input = input("Enter choice (1 / 2 or Encrypt / Decrypt): ").lower()

text = input("Enter message: ")
shift = int(input("Enter Caesar shift: "))
key = input("Enter transposition key: ")

if choice_input == '1' or choice_input == 'encrypt':
    product_encrypt(text, shift, key)

elif choice_input == '2' or choice_input == 'decrypt':
    product_decrypt(text, shift, key)

else:
    print("Invalid choice")
