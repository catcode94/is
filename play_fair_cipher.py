# Enter the message: MAYANK
# Enter the keyword (e.g., 'MONARCH'): monarch

# Prepared Text for Encryption: MAYANK
# Encrypted Message: PNZGGI
# Decrypted Message: MAYANK

import string

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        if not a.isalpha():
            i += 1
            continue

        if i + 1 < len(text):
            b = text[i + 1]
            if not b.isalpha():
                i += 1
                continue
        else:
            b = ""

        if a == b:
            prepared += a + "X"
            i += 1
        else:
            if b:
                prepared += a + b
                i += 2
            else:
                prepared += a + "X"
                i += 1

    return prepared


def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5]
            cipher += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1]
            cipher += matrix[(row2 + 1) % 5][col2]

        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]

    return cipher, matrix, text


# ----------- User Input -----------
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

ciphertext, matrix, prepared = playfair_encrypt(plaintext, key)

# ----------- Output -----------
print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

print("\nOriginal Plaintext:", plaintext)
print("Prepared Text:", prepared)
print("Ciphertext:", ciphertext)


# def create_playfair_matrix(key):
#     key = key.upper().replace(" ", "")
#     key = "".join(sorted(list(set(key)), key=key.find)) # Remove duplicates, preserve order

#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is omitted
#     key_matrix = []

#     # Add key characters to matrix
#     for char in key:
#         if char not in key_matrix and char in alphabet: # Ensure 'J' is not added if present in key
#             key_matrix.append(char)

#     # Add remaining alphabet characters
#     for char in alphabet:
#         if char not in key_matrix:
#             key_matrix.append(char)

#     matrix = []
#     for i in range(0, 25, 5):
#         matrix.append(key_matrix[i:i+5])
#     return matrix

# def prepare_text(text):
#     text = text.upper().replace(" ", "").replace("J", "I") # Uppercase, remove spaces, replace J with I
#     prepared = []
#     i = 0
#     while i < len(text):
#         if i == len(text) - 1: # Last character, add X
#             prepared.append(text[i])
#             prepared.append('X')
#             break

#         char1 = text[i]
#         char2 = text[i+1]

#         if char1 == char2: # Double letters
#             prepared.append(char1)
#             prepared.append('X')
#             i += 1
#         else:
#             prepared.append(char1)
#             prepared.append(char2)
#             i += 2
#     return "".join(prepared)

# def find_char_position(matrix, char):
#     for r in range(5):
#         for c in range(5):
#             if matrix[r][c] == char:
#                 return r, c
#     return -1,

# def playfair_encrypt(text, matrix):
#     prepared_text = prepare_text(text)
#     encrypted_text = []

#     for i in range(0, len(prepared_text), 2):
#         char1 = prepared_text[i]
#         char2 = prepared_text[i+1]

#         r1, c1 = find_char_position(matrix, char1)
#         r2, c2 = find_char_position(matrix, char2)

#         if r1 == r2: # Same row
#             encrypted_text.append(matrix[r1][(c1 + 1) % 5])
#             encrypted_text.append(matrix[r2][(c2 + 1) % 5])
#         elif c1 == c2: # Same column
#             encrypted_text.append(matrix[(r1 + 1) % 5][c1])
#             encrypted_text.append(matrix[(r2 + 1) % 5][c2])
#         else: # Rectangle
#             encrypted_text.append(matrix[r1][c2])
#             encrypted_text.append(matrix[r2][c1])

#     return "".join(encrypted_text)

# def playfair_decrypt(text, matrix):
#     decrypted_text = []

#     for i in range(0, len(text), 2):
#         char1 = text[i]
#         char2 = text[i+1]

#         r1, c1 = find_char_position(matrix, char1)
#         r2, c2 = find_char_position(matrix, char2)

#         if r1 == r2: # Same row
#             decrypted_text.append(matrix[r1][(c1 - 1 + 5) % 5])
#             decrypted_text.append(matrix[r2][(c2 - 1 + 5) % 5])
#         elif c1 == c2: # Same column
#             decrypted_text.append(matrix[(r1 - 1 + 5) % 5][c1])
#             decrypted_text.append(matrix[(r2 - 1 + 5) % 5][c2])
#         else: # Rectangle
#             decrypted_text.append(matrix[r1][c2])
#             decrypted_text.append(matrix[r2][c1])

#     return "".join(decrypted_text)

# # User Input
# message = input("Enter the message: ")
# keyword = input("Enter the keyword (e.g., 'MONARCH'): ")

# # Create Playfair matrix
# playfair_matrix = create_playfair_matrix(keyword)


# # Encrypt
# encrypted_message = playfair_encrypt(message, playfair_matrix)
# print(f"\nPrepared Text for Encryption: {prepare_text(message)}")
# print(f"Encrypted Message: {encrypted_message}")

# # Decrypt
# decrypted_message = playfair_decrypt(encrypted_message, playfair_matrix)
# print(f"Decrypted Message: {decrypted_message}")
