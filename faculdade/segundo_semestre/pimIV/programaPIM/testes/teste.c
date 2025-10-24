
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>


// #define BINARY_WRITE "wb"
// #define BINARY_READ "rb"


//teste.c
#include "biblioteca.h"
// agora => rodar esse biblioteca em um arquivo python!
int main()
{
    gravarPessoa("Kal", 22, 'M', 129);
    lerPessoa();
    return 0;
}

// gcc -o run teste.c biblioteca.c biblioteca.h | ./run


// FILE* bin_file = fopen("binary.bin", BINARY_READ);

    // if(bin_file == NULL){
    //     printf("Could not locale file\n");
    //     exit(-1);
    // }
    
    // // int number = 32;
    // // fwrite(&number, sizeof(int), 1, bin_file);

    // // double myDouble = 3.1415;
    // // fwrite(&myDouble, sizeof(double), 1, bin_file);

    // int number;
    // fread(&number, sizeof(int), 1, bin_file);

    // double myDouble;
    // fread(&myDouble, sizeof(double), 1, bin_file);

    // printf("%d\n", number);
    // printf("%lf\n", myDouble);