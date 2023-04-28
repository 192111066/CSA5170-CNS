#include <stdio.h>
#include <string.h>

void encrypt_text(char plaintext[], char key[]);

int main()
{
    char plaintext[100];
    char key[26];

    printf("Enter the plaintext to be encrypted: ");
    fgets(plaintext, 100, stdin);

    printf("Enter the substitution key (26 letters in any order): ");
    fgets(key, 26, stdin);

    encrypt_text(plaintext, key);

    printf("The encrypted text is: %s", plaintext);

    return 0;
}

void encrypt_text(char plaintext[], char key[])
{
    int i, j;

    for(i = 0; i < strlen(plaintext); i++)
    {
        
        if(plaintext[i] >= 'A' && plaintext[i] <= 'Z')
        {
            
            j = plaintext[i] - 'A';
            plaintext[i] = key[j];
        }
       
        else if(plaintext[i] >= 'a' && plaintext[i] <= 'z')
        {
            
            j = plaintext[i] - 'a';
            plaintext[i] = key[j];
        }
    }
}

