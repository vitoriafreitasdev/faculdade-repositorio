// aula 4
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");

    // Quantidade de linhas que "árvore" vai ter
    int linhas;

    printf("Quantidade de linhas: ");
    scanf("%d", &linhas);
    // Árvore feita com um laço aninhado
    int l, k;
    for (l = 1; l <= linhas; l++){

        for (k = 1; k <= l; k++){
            printf("*");
        }
        printf("\n");
    }



    return 0;

}
