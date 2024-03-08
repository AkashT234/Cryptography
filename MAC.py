#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

int main() {
    char keyword[] = "CIPHER";
    char plaintext[] = "THIS IS A SECRET MESSAGE";
    char ciphertext[100];
    int keyword_length = strlen(keyword);
    int ciphertext_length = strlen(plaintext);
    char cipher_seq[ALPHABET_SIZE] = {0};
    int i, j, k;

    for (i = 0; i < keyword_length; i++) {
        cipher_seq[toupper(keyword[i]) - 'A'] = 1;
    }
    for (i = 0, j = 0; i < ALPHABET_SIZE; i++) {
        if (cipher_seq[i] == 0) {
            keyword[keyword_length + j] = 'A' + i;
            cipher_seq[i] = 1;
            j++;
        }
    }
    keyword[keyword_length + j] = '\0';

    for (i = 0; i < ciphertext_length; i++) {
        if (isalpha(plaintext[i])) {
            k = toupper(plaintext[i]) - 'A';
            ciphertext[i] = isupper(plaintext[i]) ? toupper(keyword[k]) : tolower(keyword[k]);
        } else {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[i] = '\0';

    printf("Keyword: %s\n", keyword);
    printf("Plaintext: %s\n", plaintext);
    printf("Ciphertext: %s\n", ciphertext);

    return 0;
}