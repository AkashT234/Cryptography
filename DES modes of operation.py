BLOCK_SIZE = 8

def ecb_encrypt(plaintext, key):
    ciphertext = b''
    for i in range(0, len(plaintext), BLOCK_SIZE):
        block = plaintext[i:i + BLOCK_SIZE]
        if len(block) < BLOCK_SIZE:
            block += b'\0' * (BLOCK_SIZE - len(block))  # Padding
        encrypted_block = bytes(block_byte ^ key_byte for block_byte, key_byte in zip(block, key))
        ciphertext += encrypted_block
    return ciphertext

def main():
    plaintext = b"This is a test message."
    key = b"secretke"
    encrypted_text = ecb_encrypt(plaintext, key)
    print("Ciphertext:", encrypted_text)

if __name__ == "__main__":
    main()
