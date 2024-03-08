def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            shifted = (ord(char) - start + shift) % 26
            if decrypt:
                result += chr((ord(char) - start - shift) % 26 + start)
            else:
                result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    text = input("Enter the text to encrypt/decrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
