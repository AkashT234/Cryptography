def rail_fence(text, rails, action='encrypt'):
    if action == 'encrypt':
        fence = [[] for _ in range(rails)]
        rail, direction = 0, 1

        for char in text:
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        return ''.join([''.join(rail) for rail in fence])
    else:
        fence = [['' for _ in range(len(text))] for _ in range(rails)]
        rail, direction, index = 0, 1, 0

        for i in range(len(text)):
            fence[rail][i] = '*'
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        for i in range(rails):
            for j in range(len(text)):
                if fence[i][j] == '*' and index < len(text):
                    fence[i][j] = text[index]
                    index += 1

        rail, direction, decrypted_text = 0, 1, ''
        for i in range(len(text)):
            decrypted_text += fence[rail][i]
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

        return decrypted_text

# Example usage:
plaintext = "MEET ME AT TO NIGHT"
rails = 3

# Encrypt
encrypted_text = rail_fence(plaintext, rails)
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = rail_fence(encrypted_text, rails, action='decrypt')
print("Decrypted:", decrypted_text)
