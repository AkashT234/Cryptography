def generate_cipher_mapping(key):
    key = key.upper()
    return {chr(65 + i): key[i % len(key)] for i in range(26)}

def encrypt(text, key):
    mapping = generate_cipher_mapping(key)
    return ''.join(mapping.get(char.upper(), char) for char in text)

def decrypt(text, key):
    mapping = generate_cipher_mapping(key)
    reverse_mapping = {v: k for k, v in mapping.items()}
    return ''.join(reverse_mapping.get(char.upper(), char) for char in text)

def main():
    key = input("Enter the key for monoalphabetic cipher: ")
    text = input("Enter the text to encrypt/decrypt: ")
    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
