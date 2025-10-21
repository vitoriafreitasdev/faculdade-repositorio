
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define BINARY_WRITE "wb"
#define BINARY_READ "rb"

typedef struct 
{
   char nome[50];
   int idade;
   char sexo;
   float pressao_sanguinia;
} Pessoa;

void gravarPessoa() {
    Pessoa pessoa;
    strcpy(pessoa.nome, "Manuel");
    pessoa.idade = 26;
    pessoa.sexo = 'M';
    pessoa.pressao_sanguinia = 128;

    FILE *arquivo = fopen("pessoa.bin", "wb");

    if(arquivo == NULL){
        printf("Erro ao abrir arquivo!\n");
        return;
    }

    fwrite(&pessoa, sizeof(pessoa), 1, arquivo);
    fclose(arquivo);

    printf("Dados gravados com sucesso!\n");

}

void lerPessoa() {
    Pessoa pessoa;

    FILE *arquivo = fopen("pessoa.bin", "rb");
    if (arquivo == NULL) {
        printf("Erro ao abrir arquivo!\n");
        return;
    }

    fread(&pessoa, sizeof(pessoa), 1, arquivo);
    fclose(arquivo);

    printf("\nDados lidos do arquivo:\n");
    printf("Nome: %s\n", pessoa.nome);
    printf("Idade: %d\n", pessoa.idade);
    printf("Sexo: %c\n", pessoa.sexo);
    printf("Pressao sanguinia: %.1f\n", pessoa.pressao_sanguinia);

}

int main()
{
    gravarPessoa();
    lerPessoa();
    return 0;
}


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