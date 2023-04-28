#include <stdio.h>
#include <string.h>

#define MATRIX_SIZE 5

void generate_keymatrix(char key[], char keymatrix[MATRIX_SIZE][MATRIX_SIZE]);
void encrypt_text(char plaintext[], char keymatrix[MATRIX_SIZE][MATRIX_SIZE]);

int main()
{
    char plaintext[100];
    char key[26];
    char keymatrix[MATRIX_SIZE][MATRIX_SIZE];

    printf("Enter the plaintext to be encrypted: ");
    fgets(plaintext, 100, stdin);

    printf("Enter the keyword (up to 25 letters): ");
    fgets(key, 26, stdin);

    // Remove any newline characters from the input strings
    strtok(plaintext, "\n");
    strtok(key, "\n");

    generate_keymatrix(key, keymatrix);
    encrypt_text(plaintext, keymatrix);

    printf("The encrypted text is: %s", plaintext);

    return 0;
}

// Function to generate the key matrix from the keyword
void generate_keymatrix(char key[], char keymatrix[MATRIX_SIZE][MATRIX_SIZE])
{
    int i, j, k, len;
    char alphabet[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

    len = strlen(key);

    // Copy the keyword into the first row of the key matrix
    for(i = 0, k = 0; i < MATRIX_SIZE && k < len; i++)
    {
        for(j = 0; j < MATRIX_SIZE; j++)
        {
            if(k < len)
            {
                keymatrix[i][j] = key[k];
                k++;
            }
            else
            {
                break;
            }
        }
    }

    // Fill the remaining cells of the key matrix with the remaining letters of the alphabet
    for(i = 0, k = 0; i < MATRIX_SIZE; i++)
    {
        for(j = 0; j < MATRIX_SIZE; j++)
        {
            if(k < len && alphabet[k] == keymatrix[i][j])
            {
                k++;
            }
            else
            {
                keymatrix[i][j] = alphabet[k];
                k++;
            }
        }
    }
}

// Function to encrypt the plaintext using the key matrix
void encrypt_text(char plaintext[], char keymatrix[MATRIX_SIZE][MATRIX_SIZE])
{
    int i, j, x1, y1, x2, y2, len;
    char c1, c2;

    len = strlen(plaintext);

    // Iterate over the plaintext two characters at a time
    for(i = 0; i < len; i += 2)
    {
        // Find the positions of the two characters in the key matrix
        for(j = 0; j < MATRIX_SIZE; j++)
        {
            for(int k = 0; k < MATRIX_SIZE; k++)
            {
                if(keymatrix[j][k] == plaintext[i])
                {
                    x1 = j;
                    y1 = k;
                }
                if(keymatrix[j][k] == plaintext[i+1])
                {
                    x2 = j;
                    y2 = k;
                }
            }
        }

        // Determine the ciphertext pair based on the positions in the key matrix
        if(x1 == x2)
        {
            // Characters are in the same row - shift right and wrap around if necessary
            c1 = keymatrix[x1][(y1+1) % MATRIX_SIZE];
            c2 = keymatrix[x2][(y2+1) % MATRIX_SIZE];
        }
        else if(y1 == y2)
        {
            // Characters are in the same column - shift down and wrap around if

