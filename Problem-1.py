# f = open("raw_text.txt", "r")

# text = f.read()
# f.close()
# print(text)
# text_len = len(text)

# # find the index using an index variable, set it as 0 first
# def encryption(shift1, shift2):
#     index = 0
#     encrypted_text = ''
#     for letter in text:
#         if 'a' <= letter <= 'm':
#             pos = ord(letter) - ord('a')
#             new_pos = (pos + (shift1 * shift2)) % 26
#             encrypted_text += chr(new_pos + ord('a'))
#         elif 'n' <= letter <= 'z':
#             pos = ord(letter) - ord('a')
#             new_pos = (pos - (shift1 + shift2)) % 26
#             encrypted_text += chr(new_pos + ord('a'))
#         elif 'A' <= letter <= 'M':
#             pos = ord(letter) - ord('A')
#             new_pos = (pos - shift1) % 26
#             encrypted_text += chr(new_pos + ord('A'))
#         elif 'N' <= letter <= 'Z':
#             pos = ord(letter) - ord('A')
#             new_pos = (pos + (shift2 ** 2)) % 26
#             encrypted_text += chr(new_pos + ord('A'))
#         else:
#             encrypted_text += letter
#         index += 1
#     return encrypted_text

# def decryption(shift1, shift2, text):
#     index = 0
#     decrypted_text = ''
#     for letter in text:
#         print(letter)
#         if 'a' <= letter <= 'm':
#             pos = ord(letter) - ord('a')
#             new_pos = (pos - (shift1 * shift2)) % 26
#             decrypted_text += chr(new_pos + ord('a'))
#         elif 'n' <= letter <= 'z':
#             pos = ord(letter) - ord('a')
#             new_pos = (pos + (shift1 + shift2)) % 26
#             decrypted_text += chr(new_pos + ord('a'))
#         elif 'A' <= letter <= 'M':
#             pos = ord(letter) - ord('A')
#             new_pos = (pos + shift1) % 26
#             decrypted_text += chr(new_pos + ord('A'))
#         elif 'N' <= letter <= 'Z':
#             pos = ord(letter) - ord('A')
#             new_pos = (pos - (shift2 ** 2)) % 26
#             decrypted_text += chr(new_pos + ord('A'))
#         else:
#             decrypted_text += letter
#         index += 1
#     return decrypted_text

# def verification():
#     f4 = open("raw_text.txt", "r")
#     raw_text = f4.read()
#     f4.close()

#     f5 = open("decrypted_text.txt", "r")
#     decrypted_text = f5.read()
#     f5.close()

#     return raw_text == decrypted_text

# key1 = int(input("Enter the shift1 value: "))
# key2 = int(input("Enter the shift2 value: "))

# encrypted_text = encryption(key1, key2)
# print(encrypted_text)

# # Writes new encrypted content
# f2 = open("encrypted_text.txt", "w")
# f2.write(encrypted_text)
# f2.close()


# decrypted_text = decryption(key1, key2, encrypted_text)
# print(decrypted_text)

# # Writes new decrypted content
# f3 = open("decrypted_text.txt", "w")
# f3.write(decrypted_text)
# f3.close()

# if verification():
#     print("The decryption is successful.")
# else:
#     print("The decryption is unsuccessful.")

## keep the old code
## here is the new one that satisfy the logic

RAW_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)/raw_text.txt"
ENCRYPTED_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)/encrypted_text.txt"
DECRYPTED_PATH = "/Users/mamunudoy/Downloads/Assignment 2 (1)/decrypted_text.txt"


def encrypt_text(shift1, shift2):
    with open(RAW_PATH, "r", encoding = "utf-8") as file:
        raw_text = file.read()
    encrypted = []
    direction_array = [] #1- forward and 0- for backward

    for ch in raw_text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
                direction_array.append(1)
            elif 'n' <= ch <= 'z':
                shift = shift1 + shift2
                new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
                direction_array.append(0)
            encrypted.append(new_char)

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                shift = shift1
                new_char = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
                direction_array.append(0)
            elif 'N' <= ch <= 'Z':
                shift = shift2 ** 2
                new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
                direction_array.append(1)
            encrypted.append(new_char)

        else:
            encrypted.append(ch)
            direction_array.append(None)

    encrypted_text = "".join(encrypted)

    with open(ENCRYPTED_PATH, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    return raw_text, encrypted_text, direction_array



def decrypt_text(direction_array, shift1, shift2):
    with open(ENCRYPTED_PATH, "r", encoding="utf-8") as file:
        encrypted_text = file.read()

    decrypted = []

    for i, ch in enumerate(encrypted_text):
        direction = direction_array[i]

        if direction is None:
            decrypted.append(ch)
            continue

        if ch.islower():
            if direction == 1:
                shift = shift1 * shift2
                new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            else:
                shift = shift1 + shift2
                new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            decrypted.append(new_char)

        elif ch.isupper():
            if direction == 1:
                shift = shift2 ** 2
                new_char = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                shift = shift1
                new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            decrypted.append(new_char)

    decrypted_text = "".join(decrypted)

    with open(DECRYPTED_PATH, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    return decrypted_text


def verify_decryption(raw_text, decrypted_text):
    return raw_text == decrypted_text



#Main method
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

raw_text, encrypted_text, direction_array = encrypt_text(shift1,shift2)
decrypted_text = decrypt_text(direction_array, shift1, shift2)

# print("\n------ RAW TEXT ------")
# print(raw_text)

# print("\n--- ENCRYPTED TEXT ---")
# print(encrypted_text)

# print("\n--- DECRYPTED TEXT ---")
# print(decrypted_text)

if verify_decryption(raw_text, decrypted_text):
    print("\n Decryption successful.Text matches original.")
else:
    print("\n Decryption failed.")






