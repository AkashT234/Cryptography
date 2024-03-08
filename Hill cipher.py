import numpy as np

def encrypt_hill_cipher(plaintext, key_matrix):
    block_size = len(key_matrix)
    # Convert plaintext to numerical values
    plaintext_num = [ord(char) - ord('A') for char in plaintext]
    
    # Pad the plaintext if its length is not a multiple of the block size
    if len(plaintext_num) % block_size != 0:
        padding_length = block_size - (len(plaintext_num) % block_size)
        plaintext_num += [0] * padding_length
    
    ciphertext = ""
    for i in range(0, len(plaintext_num), block_size):
        block = np.array(plaintext_num[i:i + block_size])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(val + ord('A')) for val in encrypted_block)
    
    return ciphertext

# Example usage
plaintext = "HELP"
key_matrix = np.array([[3, 3], [2, 5]])
ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
print("Ciphertext:", ciphertext)