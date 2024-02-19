import sys

# takes the first argument and put it in flag
flag = sys.argv[1]

converted_chars = []

# to reverse the decryption, we will split each of the 16 bit character to 2 8 bit character
# we loop through the character and get the character and store in array

for char in flag:
    biner = ord(char)

    # shift right by 8 bits and mask to keep only the first 8 bits
    first_8bit = (biner >> 8) & 0xFF

    # mask to keep only the last 8 bits
    last_8bit = biner & 0xFF

    # store in array
    converted_chars.append(chr(first_8bit))
    converted_chars.append(chr(last_8bit))

# concatenate the characters
result = ''.join(converted_chars)

#print
print(result)