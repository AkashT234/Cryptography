def generate_playfair_key(key):
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # excluding 'J'
    remaining_chars = [char for char in alphabet if char not in key_set]

    playfair_key = list(key) + remaining_chars
    playfair_matrix = [playfair_key[i:i+5] for i in range(0, 25, 5)]

    return playfair_matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_playfair(plaintext, key):
    # Preprocess the plaintext
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    # Generate the Playfair key matrix
    playfair_matrix = generate_playfair_key(key)

    # Create digraphs from the plaintext
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    if len(digraphs[-1]) == 1:  # If the last digraph has only one letter, add 'X'
        digraphs[-1] += 'X'

    # Encrypt digraphs
    ciphertext = ""
    for digraph in digraphs:
        row1, col1 = find_position(playfair_matrix, digraph[0])
        row2, col2 = find_position(playfair_matrix, digraph[1])

        if row1 == row2:  # Same row
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5] + playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1] + playfair_matrix[(row2 + 1) % 5][col2]
        else:  # Forming a rectangle
            ciphertext += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

    return ciphertext

# Example usage
key = "NETWORK"
plaintext = "MOSQUE"
ciphertext = encrypt_playfair(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
