def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            if decrypt:
                shift = -shift
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
            key_index += 1
        else:
            result += char
    return result

def main():
    text = input("Enter the text to encrypt/decrypt: ")
    key = input("Enter the key for Vigenere cipher: ")
    encrypted_text = vigenere_cipher(text, key)
    decrypted_text = vigenere_cipher(encrypted_text, key, decrypt=True)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
