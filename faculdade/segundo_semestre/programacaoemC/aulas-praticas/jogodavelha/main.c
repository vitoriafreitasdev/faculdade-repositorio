#include <stdio.h>
#include <stdlib.h>

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


    mat[0][2] = 'X';

    for (i = 0; i < 3; i++){
        for (j = 0; j < 3; j++){
            printf("%c", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
