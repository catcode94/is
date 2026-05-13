# Option 1 : encryption

# Option 2 : decryption

# choose option : 1
# Enter text : MAYANK
# Enter shift value : 3
# Encrypted text : 
#  (array([['M', '', '', '', 'N', ''],
#        ['', 'A', '', 'A', '', 'K'],
#        ['', '', 'Y', '', '', '']], dtype='<U1'), 'MNAAKY')

# first code ko aise:
# Enter the plaintext: hello world
# Enter the key (number of rails): 2

# Original Plaintext: hello world
# Encrypted Text: hlowrdel ol
# Decrypted Text: hello world
def rail_fence_decrypt(ciphertext, key):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]

    dir_down = False
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*':
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    dir_down = False

    for _ in range(len(ciphertext)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        if rail[row][col] != '\n':
            result.append(rail[row][col])

        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

plaintext_input = input("Enter the plaintext: ")
key_input = int(input("Enter the key (number of rails): "))

encrypted_text_user = rail_fence_encrypt(plaintext_input, key_input)
decrypted_text_user = rail_fence_decrypt(encrypted_text_user, key_input)

print(f"\nOriginal Plaintext: {plaintext_input}")
print(f"Encrypted Text: {encrypted_text_user}")
print(f"Decrypted Text: {decrypted_text_user}")



# def rail_frnce_cipher_encrypt(text,shift_value):
#   import numpy as np
#   result=''

#   row=shift_value
#   col=int(len(text))

#   arr=np.empty([row,col],dtype='str')

#   r=0
#   dir='down'

#   for i in range (0, col):
#     if(text[i]==" "):
#       arr[r][i]=" "
#     else:
#       arr[r][i]=text[i]

#     if (r==row-1):
#       dir='up'
#     if(r==0):
#       dir='down'

#     if(dir=='down'):
#       r+=1
#     else:
#       r-=1

#   for i in range (0,row):
#     for j in range (0,col):
#          result+=arr[i][j]


#   return arr,result


# def rail_frnce_cipher_decrypt(text,shift_value):
#   import numpy as np
#   result=''
#   row=shift_value
#   col=int(len(text))

#   arr=np.empty([row,col],dtype='str')

#   r=0
#   dir='down'

#   for i in range (0, col):
#     if(text[i]==" "):
#       arr[r][i]=" "
#     else:
#       arr[r][i]=text[i]

#     if (r==row-1):
#       dir='up'
#     if(r==0):
#       dir='down'

#     if(dir=='down'):
#       r+=1
#     else:
#       r-=1

#   index=0
#   for i in range (0,row):
#     for j in range (0,col):
#          if(str(arr[i][j])):
#           arr[i][j]=text[index]
#           index+=1

#   r=0
#   dir='down'

#   for i in range (0, col):
#     if(str(arr[r][i])):
#        result+=arr[r][i]

#     if (r==row-1):
#       dir='up'
#     if(r==0):
#       dir='down'

#     if(dir=='down'):
#       r+=1
#     else:
#       r-=1

#   return arr,result



# print("Option 1 : encryption\n")
# print("Option 2 : decryption\n")

# option=int(input("choose option : "))


# text=str(input("Enter text : "))
# shift_value=int(input("Enter shift value : "))

# if (option==1):
#     print("Encrypted text : \n",rail_frnce_cipher_encrypt(text, shift_value))

# if (option==2):
#     print("Decrypted text : \n",rail_frnce_cipher_decrypt(text, shift_value))
