#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");
    // exerc 1
    int notas[5];
    notas[0] = 1;
    notas[1] = 2;
    notas[2] = 3;
    notas[3] = 4;
    notas[4] = 5;

    // exerc 2

    int idades[3] = {10, 20, 30};


    // exerc 3
    int tam;


    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tam);

    int vetor_exemplo[tam];

    int i, vetor[10];

    for(i = 0; i < 10; i++){
        printf("Digite o %d valor: ", i+1);
        scanf("%d", &vetor[i]);
    }


    printf("%d ", vetor[0]);
    printf("%d ", vetor[1]);

//    for para mostrar o vetor

    int tamanho = sizeof(vetor)/ sizeof(vetor[0]);

    int j = 0;
    for (j; j < tamanho; j++){
        printf("%d ", vetor[j] );
    }



    // exerc 4

    int nota[5];

    nota[0] = 10;
    nota[1] = 8;
    nota[2] = 9;
    nota[3] = 7;
    nota[4] = 6;

    printf("Nota da terceira posição: %d\n", nota[2]);

    // exerc 5

    int t, tamanho_vetor = 3;
    int array[tamanho_vetor];

    array[0] = 1;
    array[1] = 2;
    array[2] = 3;

    for (t = 0; t < tamanho_vetor; t++){
        printf("%d ", array[t]);
    }

    // exerc 6

    int s, valores[5], soma = 0;
    float media;

    for(s = 0; s < 5; s++){
        printf("\nDigite o valor %d: ", s + 1);
        scanf("%d", &valores[s]);
        soma += valores[s];
    }

    media = soma / 5.0;

    printf("\nSoma: %d\n", soma);
    printf("\nMédia: %.2f\n", media);

    // desafio

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
