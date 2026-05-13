# Enter E for Encrypt or D for Decrypt: E
# Enter message: Information Security 
# Enter key: JEHGYTHFG
# Ciphertext: DNVSSVCKNZDRKICSENKLD

import numpy as np
import math

#ENCRYPT

keyMatrix = []
messageVector = []
cipherMatrix = []

def getKeyMatrix(key, size):
    global keyMatrix
    keyMatrix = [[0] * size for _ in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1


def encrypt(messageVector, size):
    global cipherMatrix
    cipherMatrix = [[0] for _ in range(size)]
    for i in range(size):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(size):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26


def HillEncrypt(message, key):

    size = int(math.sqrt(len(key)))

    if size * size != len(key):
        print("Key is not a square matrix")
        return

    if len(message) % size != 0:
        pad = size - (len(message) % size)
        message += 'X' * pad
        print("Padded message:", message)

    getKeyMatrix(key, size)

    CipherText = []

    for s in range(0, len(message), size):

        messageVector = [[0] for _ in range(size)]

        for i in range(size):
            messageVector[i][0] = ord(message[s+i]) - 65

        encrypt(messageVector, size)

        for i in range(size):
            CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext:", "".join(CipherText))


#DECRYPT

def getKeyMatrixDecrypt(key):
    size = int(len(key) ** 0.5)

    if size * size != len(key):
        print("Key is not square")
        return None

    keyMatrix = [[ord(key[i*size + j]) % 65 for j in range(size)] for i in range(size)]
    return np.array(keyMatrix)


def inverseKey(keyMatrix):

    det = round(np.linalg.det(keyMatrix))
    det = (det % 26 + 26) % 26

    detInv = None
    for x in range(1, 26):
        if (det * x) % 26 == 1:
            detInv = x
            break

    if detInv is None:
        print("Inverse does not exist")
        return None

    size = keyMatrix.shape[0]
    adj = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):

            minor = np.delete(np.delete(keyMatrix, i, axis=0), j, axis=1)

            cofactor = round(np.linalg.det(minor))

            sign = (-1) ** (i + j)

            adj[j][i] = (sign * cofactor) % 26

    invKey = (detInv * adj) % 26

    return invKey


def HillDecrypt(cipher, key):

    keyMatrix = getKeyMatrixDecrypt(key)

    if keyMatrix is None:
        return

    size = keyMatrix.shape[0]

    invKey = inverseKey(keyMatrix)

    if invKey is None:
        return

    cipher = cipher.upper()

    if len(cipher) % size != 0:
        cipher += 'X' * (size - len(cipher) % size)

    result = ""

    for i in range(0, len(cipher), size):
        block = cipher[i:i+size]

        vec = np.array([[ord(c) - 65] for c in block])

        res = np.dot(invKey, vec) % 26

        result += "".join(chr(int(x) + 65) for x in res)

    print("Decrypted Text:", result)




if __name__ == "__main__":

    choice = input("Enter E for Encrypt or D for Decrypt: ").upper()

    if choice == "E":
        message = input("Enter message: ").upper()
        key = input("Enter key: ").upper()
        HillEncrypt(message, key)

    elif choice == "D":
        cipher = input("Enter cipher text: ").upper()
        key = input("Enter key: ").upper()
        HillDecrypt(cipher, key)

    else:
        print("Invalid choice")
