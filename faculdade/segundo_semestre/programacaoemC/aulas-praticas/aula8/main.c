#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");

    int x = 10;

    int *p;

    p = &x; // vai receber o endereço de x

    printf("Valor de x = %d\n", x);
    printf("Endereço de x = %p\n", &x);
    printf("Endereço armazenado em p = %p\n", p);
    printf("Valor apontado por p = %d\n", *p);

    // exemplo 2

    int X = 10;
    int *P = &X;

    printf("Valor de x: %d\n", X);
    printf("Endereço de x: %p\n", &X);
    printf("Valor apontado por p: %d\n", *P);

    *P = 200;

    printf("Novo valor de x: %d\n", X);
    printf("Valor apontado por p: %d\n", *P);

    // exemplo 3

    FILE *arquivo = fopen("dados.txt", "w");

    if(arquivo != NULL){
        fprintf(arquivo, "Olá, mundo!\n");
        fclose(arquivo);
        printf("Arquivo escrito com secesso.\n");
    }
    else {
        printf("Erro ao abrir o arquivo.\n");
    }

    // exemplo 4

    FILE *arq = fopen("dados.txt", "r");
    char linha[100];

    if(arq != NULL) {
        while(fgets(linha, 100, arq) != NULL){
            printf("%s", linha);
        }
        fclose(arq);
    } else {
        printf("Erro ao ler o arquivo.\n");
    }

    // desafio

    char nome[50];
    int idade;

    printf("Seu nome: ");
    fgets(nome, sizeof(nome), stdin);

    printf("Sua idade: ");
    scanf("%d", &idade);

    FILE *arquivo_usuario = fopen("cadastro.txt", "w");

    if (arquivo_usuario != NULL) {
        fprintf(arquivo_usuario, "Nome: %sIdade: %d", nome, idade);
        fclose(arquivo);
        printf("Arquivo escrito com sucesso.\n");
    } else {
        printf("Error ao abrir o arquivo.\n");

    }

    FILE *leitura = fopen("cadastro.txt", "r");
    char linhas[100];
    printf("Leitura do arquivo\n");
    if (arquivo_usuario != NULL) {
        while(fgets(linhas, 100, arquivo_usuario) != NULL){
            printf("%s", linhas);
        }
    } else {
        printf("Error ao abrir o arquivo.\n");

    }

    return 0;
}
