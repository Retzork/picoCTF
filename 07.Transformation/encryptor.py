import sys

# takes the first argument and put it in flag
flag = sys.argv[1]

converted_chars = []

# loop through all char. each two char is combined to one
# the typical character is using 8 bit, but there is a character that uses 16 bit
# so using 2 8 bit character we combine it to 1 16 bit character

for i in range(0, len(flag), 2):

    char1 = flag[i]
    char2 = flag[i + 1]

    # we combine with + sign, but we convert it to binary first
    # convert 1st char to binary, then shift it to the left 8 times
    # then combine with the binary of the 2nd char
    combined_unicode = (ord(char1) << 8) + ord(char2)
    
    # convert the binary to char then store
    combined_char = chr(combined_unicode)
    converted_chars.append(combined_char)

# concatenate the characters
result = ''.join(converted_chars)

#print
print(result)

# original encryptor. they basically do the same thing
# print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))