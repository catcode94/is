# Enter text to Cipher :mayank
# Cipher Map: 
#  {'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'}
# Encrypted: DQNQFA
# Decrypted: MAYANK

import string

def encrypt(plaintext, key):
    alphabet = string.ascii_uppercase
    # Create mapping: A->Q, B->W, etc.
    cipher_map = dict(zip(alphabet, key.upper()))
    print("Cipher Map: \n", cipher_map)
    return ''.join(cipher_map.get(char, char) for char in plaintext.upper())

def decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    # Reverse mapping: Q->A, W->B, etc.
    cipher_map = dict(zip(key.upper(), alphabet))
    return ''.join(cipher_map.get(char, char) for char in ciphertext.upper())

# Example
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
plaintext = input("Enter text to Cipher :")
ciphertext = encrypt(plaintext, key) # Output: ITSSG VGksR
print("Encrypted:", ciphertext)
print("Decrypted:", decrypt(ciphertext, key))
