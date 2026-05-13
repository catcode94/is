"""
=== Row Transposition Cipher ===
Enter message: MAYANK
Enter key (example: SECRET): qwerty

--- ENCRYPTION ---

Prepared Message: MAYANK

Grid (row-wise filling):
['M', 'A', 'Y', 'A', 'N', 'K']

Column order based on key: ['E', 'Q', 'R', 'T', 'W', 'Y']
Encrypted: YMANAK

--- DECRYPTION ---

Column order for filling: ['E', 'Q', 'R', 'T', 'W', 'Y']

Grid (column-wise filling):
['M', 'A', 'Y', 'A', 'N', 'K']
Decrypted: MAYANK
"""

def encrypt_row_transposition(message, key):
    # Step 1: Clean the message
    message = message.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)
    rows = (len(message) + cols - 1) // cols  # number of rows

    # Step 2: Add padding if needed
    message += 'X' * (rows * cols - len(message))

    print("\nPrepared Message:", message)

    # Step 3: Fill grid row-wise
    grid = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        grid.append(row)

    print("\nGrid (row-wise filling):")
    for row in grid:
        print(row)

    # Step 4: Sort key to decide column order
    order = sorted(range(len(key)), key=lambda k: key[k])

    print("\nColumn order based on key:", [key[i] for i in order])

    # Step 5: Read columns to create ciphertext
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

    # Step 1: Empty grid
    grid = [['' for _ in range(cols)] for _ in range(rows)]

    # Step 2: Same column order
    order = sorted(range(len(key)), key=lambda k: key[k])

    print("\nColumn order for filling:", [key[i] for i in order])

    # Step 3: Fill column-wise
    index = 0
    for col in order:
        for r in range(rows):
            grid[r][col] = cipher[index]
            index += 1

    print("\nGrid (column-wise filling):")
    for row in grid:
        print(row)

    # Step 4: Read row-wise to get message
    message = ""
    for r in range(rows):
        for c in range(cols):
            message += grid[r][c]

    # Step 5: Remove padding
    return message.rstrip('X')


# Main program
print("=== Row Transposition Cipher ===")

msg = input("Enter message: ")
key = input("Enter key (example: SECRET): ")

print("\n--- ENCRYPTION ---")
encrypted = encrypt_row_transposition(msg, key)
print("Encrypted:", encrypted)

print("\n--- DECRYPTION ---")
decrypted = decrypt_row_transposition(encrypted, key)
print("Decrypted:", decrypted)
