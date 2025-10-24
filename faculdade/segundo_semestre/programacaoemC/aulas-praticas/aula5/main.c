#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");
    int vet[10], total = 0, v;
    float media_vet;

    for (v = 0; v < 10; v++){
        printf("\nDigite um valor: ");
        scanf("%d", &vet[v]);
        total += vet[v];
    }

    media_vet = total / 10.0;

    printf("\nMédia: %.2f", media_vet);
    printf("\nSoma: %d", total);
    printf("\nValores pares: ");
    int n;
    for (n = 0; n < 10; n++){
        if(vet[n] % 2 == 0){
            printf("%d ", vet[n]);
        }
    }

    return 0;


}
