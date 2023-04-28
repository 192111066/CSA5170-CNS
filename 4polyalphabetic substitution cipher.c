#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generate_key(char key[], int keylen);
void encrypt_text(char plaintext[], char key[], int keylen);

int main()
{
    char plaintext[100];
    char key[26];
    int keylen;

    printf("Enter the plaintext to be encrypted: ");
    fgets(plaintext, 100, stdin);

    printf("Enter the key (up to 25 letters): ");
    fgets(key, 26, stdin);

    // Remove any newline characters from the input strings
    strtok(plaintext, "\n");
    strtok(key, "\n");

    keylen = strlen(key);

    generate_key(key, keylen);
    encrypt_text(plaintext, key, keylen);

    printf("The encrypted text is: %s", plaintext);

    return 0;
}

// Function to generate the full key string by repeating the original key
void generate_key(char key[], int keylen)
{
    int i, j, k;

    // Determine the length of the plaintext
    int plaintextlen = strlen(plaintext);

    // Repeat the key until it is at least as long as the plaintext
    for(i = keylen; i < plaintextlen; i++)
    {
        key[i] = key[i-keylen];
    }
    key[i] = '\0';
}

// Function to encrypt the plaintext using the polyalphabetic substitution cipher
void encrypt_text(char plaintext[], char key[], int keylen)
{
    int i, j, len;
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char ciphertext[100];

    len = strlen(plaintext);

    // Iterate over the plaintext character by character
    for(i = 0; i < len; i++)
    {
        // Find the index of the current plaintext character in the alphabet
        int plainidx = strchr(alphabet, plaintext[i]) - alphabet;

        // Find the index of the current key character in the alphabet
        int keyidx = strchr(alphabet, key[i % keylen]) - alphabet;

        // Determine the ciphertext character by shifting the plaintext character by the key index
        int cipheridx = (plainidx + keyidx) % 26;

        // Append the ciphertext character to the ciphertext string
        ciphertext[i] = alphabet[cipheridx];
    }

    // Null-terminate the ciphertext string and copy it back to the plaintext string
    ciphertext[len] = '\0';
    strcpy(plaintext, ciphertext);
}

