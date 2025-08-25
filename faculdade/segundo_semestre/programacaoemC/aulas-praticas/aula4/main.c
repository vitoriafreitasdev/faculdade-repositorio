// aula 4
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");

    int i = 0;

    while(i <= 5){
        printf("%d\n", i);
        i++;
    }
    //

    char opcao;

    do {
        printf("Deseja continuar? (s/n): ");
        scanf(" %c", &opcao);
    } while (opcao == 's' || opcao == 'S');

    printf("Fim do programa.\n");

    //

    int I;
    for (I = 1; I <= 5; I++){
        printf("Valor: %d\n", I);
    }


    //

    int o, j;

    for(o = 1; o <= 10; o++){
        printf("\nTabuada do %d:\n", o);

        for(j = 1; j <= 10; j++){
            printf("%d x %d = %d\n", o, j, o * j);
        }

    }
    // desafio

    float numero;
    float soma;
    float media;
    int quantidade = 0;

    while(numero != 0){
        printf("Digite um numero: ");
        scanf("%f", &numero);
        if(numero > 0){
            soma += numero;
            quantidade++;
        }
    }

    media = soma / quantidade;

    printf("Media: %.2f\n", media);

    // desafio

    int linhas;

    printf("Quantidade de linhas: ");
    scanf("%d", &linhas);

    int l, k;
    for (l = 1; l <= linhas; l++){

        for (k = 1; k <= l; k++){
            printf("*");
        }
        printf("\n");
    }



    return 0;
}
