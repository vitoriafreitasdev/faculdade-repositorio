#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main()
{
    char mat[3][3] =
    {
    {'1', '2', '3'},    // Use aspas simples para caracteres
    {'4', '5', '6'},
    {'7', '8', '9'}
    };
    int i, j;

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            printf("%c", mat[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    mat[0][2] = 'X';
    mat[1][2] = 'X';
    mat[2][2] = 'X';

    bool fim = false;

    // diagonal 1
    if (mat[0][0] == 'X' && mat[1][1] == 'X' && mat[2][2] == 'X'){
        fim = true;
    }
    // diagonal 2
    if (mat[0][2] == 'X' && mat[1][1] == 'X' && mat[2][0] == 'X'){
        fim = true;
    }

    // linha 1
    if (mat[0][0] == 'X' && mat[0][1] == 'X' && mat[0][2] == 'X'){
        fim = true;
    }
    // linha 2
    if (mat[1][0] == 'X' && mat[1][1] == 'X' && mat[1][2] == 'X'){
        fim = true;
    }
    // linha 3
    if (mat[2][0] == 'X' && mat[2][1] == 'X' && mat[2][2] == 'X'){
        fim = true;
    }


    // coluna 1
    if (mat[0][0] == 'X' && mat[1][0] == 'X' && mat[2][0] == 'X'){
        fim = true;
    }
    // coluna 2
    if (mat[0][1] == 'X' && mat[1][1] == 'X' && mat[2][1] == 'X'){
        fim = true;
    }
    // coluna 3
    if (mat[0][2] == 'X' && mat[1][2] == 'X' && mat[2][2] == 'X'){
        fim = true;
    }

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            printf("%c", mat[i][j]);
        }
        printf("\n");
    }
    if(fim){
        printf("Jogo acabou");
    }
    return 0;
}
