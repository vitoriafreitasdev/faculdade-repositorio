#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[50];
    int idade;
    char sexo;
    float pressao_sanguinia;
} Pessoa;

void gravarPessoa(const char *nome, int idade, char sexo, float pressao_sanguinia) {
    Pessoa pessoa;
    strcpy(pessoa.nome, nome);
    pessoa.idade = idade;
    pessoa.sexo = sexo;
    pessoa.pressao_sanguinia = pressao_sanguinia;

    FILE *arquivo = fopen("pessoa.bin", "wb");
    if (!arquivo) {
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