#include <stdio.h>
#include <string.h>

void encrypt_text(char plaintext[], int k);

int main()
{
    char plaintext[100];
    int k;

    printf("Enter the plaintext to be encrypted: ");
    fgets(plaintext, 100, stdin);

    printf("Enter the shift pattern (1-25): ");
    scanf("%d", &k);

    encrypt_text(plaintext, k);

    printf("The encrypted text is: %s", plaintext);

    return 0;
}

void encrypt_text(char plaintext[], int k)
{
    int i;

    for(i = 0; i < strlen(plaintext); i++)
    {
        
        if(plaintext[i] >= 'A' && plaintext[i] <= 'Z')
        {
            
            plaintext[i] = ((plaintext[i] - 'A') + k) % 26 + 'A';
        }
        
        else if(plaintext[i] >= 'a' && plaintext[i] <= 'z')
        {
        
            plaintext[i] = ((plaintext[i] - 'a') + k) % 26 + 'a';
        }
    }
}

