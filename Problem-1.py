f = open("raw_text.txt", "r")

text = f.read()
f.close()
print(text)
text_len = len(text)

# find the index using an index variable, set it as 0 first
def encryption(shift1, shift2):
    index = 0
    encrypted_text = ''
    for letter in text:
        if 'a' <= letter <= 'm':
            pos = ord(letter) - ord('a')
            new_pos = (pos + (shift1 * shift2)) % 26
            encrypted_text += chr(new_pos + ord('a'))
        elif 'n' <= letter <= 'z':
            pos = ord(letter) - ord('a')
            new_pos = (pos - (shift1 + shift2)) % 26
            encrypted_text += chr(new_pos + ord('a'))
        elif 'A' <= letter <= 'M':
            pos = ord(letter) - ord('A')
            new_pos = (pos - shift1) % 26
            encrypted_text += chr(new_pos + ord('A'))
        elif 'N' <= letter <= 'Z':
            pos = ord(letter) - ord('A')
            new_pos = (pos + (shift2 ** 2)) % 26
            encrypted_text += chr(new_pos + ord('A'))
        else:
            encrypted_text += letter
        index += 1
    return encrypted_text

def decryption(shift1, shift2, text):
    index = 0
    decrypted_text = ''
    for letter in text:
        print(letter)
        if 'a' <= letter <= 'm':
            pos = ord(letter) - ord('a')
            new_pos = (pos - (shift1 * shift2)) % 26
            decrypted_text += chr(new_pos + ord('a'))
        elif 'n' <= letter <= 'z':
            pos = ord(letter) - ord('a')
            new_pos = (pos + (shift1 + shift2)) % 26
            decrypted_text += chr(new_pos + ord('a'))
        elif 'A' <= letter <= 'M':
            pos = ord(letter) - ord('A')
            new_pos = (pos + shift1) % 26
            decrypted_text += chr(new_pos + ord('A'))
        elif 'N' <= letter <= 'Z':
            pos = ord(letter) - ord('A')
            new_pos = (pos - (shift2 ** 2)) % 26
            decrypted_text += chr(new_pos + ord('A'))
        else:
            decrypted_text += letter
        index += 1
    return decrypted_text

def verification():
    f4 = open("raw_text.txt", "r")
    raw_text = f4.read()
    f4.close()

    f5 = open("decrypted_text.txt", "r")
    decrypted_text = f5.read()
    f5.close()

    return raw_text == decrypted_text

key1 = int(input("Enter the shift1 value: "))
key2 = int(input("Enter the shift2 value: "))

encrypted_text = encryption(key1, key2)
print(encrypted_text)

# Writes new encrypted content
f2 = open("encrypted_text.txt", "w")
f2.write(encrypted_text)
f2.close()


decrypted_text = decryption(key1, key2, encrypted_text)
print(decrypted_text)

# Writes new decrypted content
f3 = open("decrypted_text.txt", "w")
f3.write(decrypted_text)
f3.close()

if verification():
    print("The decryption is successful.")
else:
    print("The decryption is unsuccessful.")



