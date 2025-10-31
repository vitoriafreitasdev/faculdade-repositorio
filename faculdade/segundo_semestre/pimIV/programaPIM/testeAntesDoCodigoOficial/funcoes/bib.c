
//bib.c
#include <math.h>
#include <stdio.h>
// formula valor_normalizado = valor_original / valor_maximo_absoluto

void sinais_normalizados(int vetor[], int tamanho, int valor_maximo_absoluto, float vetor_saida[]){
    int i;
    for(i = 0; i < tamanho; i++){
        float valor = (float)vetor[i] / valor_maximo_absoluto;
        vetor_saida[i] = roundf(valor * 100) / 100;  // Arredonda para 2 casas
    }
    
}