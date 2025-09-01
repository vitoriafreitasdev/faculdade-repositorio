#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");

    int m[3][4] = {{3, 4, 5, 5}, {1, 3, 6, 5}, {8, 1, 2, 5}};

    int i, j;
    for (i = 0; i < 3; i++){
        for(j=0; j<4; j++){
            //imprimindo a matriz
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }

    // exerc 2

    int lin = 5, col = 2;
    int matriz[5][2];
    int l, c;
    for(l = 0; l < lin; l++){
        for(c = 0; c < col; c++){
            matriz[l][c] = l + c;
        }
    }

    printf("Matriz preenchida com l + c:\n");
    for(l = 0; l < lin; l++){
        for(c = 0; c < col; c++){
            printf("%d ", matriz[l][c]);
        }
        printf("\n");
    }

    // exerc 3

    int mat[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    };

    int I, J, soma = 0;

    for(I = 0; I < 3; I++){
        for(J = 0; J < 3; J++){
            soma += mat[I][J];
        }
    }

    printf("Soma dos elementos da matriz: %d \n", soma);

    // desafio

    int matriz_usuario[3][3];
    int L, C;
    int valor;
    for (L = 0; L < 3; L++){
        for(C = 0; C < 3; C++ ) {

            printf("Digite o valor que vai na linha %d e coluna %d: ", L, C);
            scanf("%d", &valor);
            matriz_usuario[L][C] = valor;
        }
    }

    printf("Matriz criada: \n");
    int soma_total = 0;
    int soma_par = 0;
    float media;
    for (L = 0; L < 3; L++){
        for(C = 0; C < 3; C++ ) {

           printf("%d ", matriz_usuario[L][C]);

           soma_total += matriz_usuario[L][C];

           if (matriz_usuario[L][C] % 2 == 0) {

            soma_par += matriz_usuario[L][C];

           }
        }
        printf("\n");
    }
    // media de todos valores, divida pelo total de elementos, linhas x colunas

    media = soma_total / 9.0;

    printf("Soma total: %d\n", soma_total);
    printf("Soma dos pares: %d\n", soma_par);
    printf("Media: %.2f\n", media);

    return 0;
}
