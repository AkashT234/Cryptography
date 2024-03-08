#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void generateKeyStream(int keyStream[], int length) {
    srand(time(0));
    for (int i = 0; i < length; i++) {
        keyStream[i] = rand() % 27; 
    }
}

void transform(char input[], int keyStream[], char output[], int encrypt) {
    int len = strlen(input);
    for (int i = 0; i < len; i++) {
        if (input[i] >= 'A' && input[i] <= 'Z') {
            int shift = keyStream[i];
            output[i] = (input[i] - 'A' + (encrypt ? shift : -shift + 26)) % 26 + 'A';
        } else {
            output[i] = input[i];
        }
    }
    output[len] = '\0';
}

int main() {
    char plaintext[100], ciphertext[100], decryptedText[100];
    int keyStream[100], length;

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = '\0';

    length = strlen(plaintext);
    generateKeyStream(keyStream, length);

    printf("\nKey Stream: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", keyStream[i]);
    }

    transform(plaintext, keyStream, ciphertext, 1);
    printf("\n\nCiphertext: %s", ciphertext);

    transform(ciphertext, keyStream, decryptedText, 0);
    printf("\nDecrypted Text: %s", decryptedText);

    return 0;
}
