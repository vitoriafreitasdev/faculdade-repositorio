#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");

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

    return 0;
}
