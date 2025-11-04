
// arquivo main.c
#include <stdio.h>
#include <stdlib.h>
#include "bib.h"

int main(){
  
    int vetor[7] = {-32700, -15000, -8000, 0, 12000, 25000, 31000};
    float vetor_saida[7];
    int i;
    //pré-processamento
    sinais_normalizados(vetor, 7, 32767, vetor_saida);
    printf("Resultado do pre-processamento\n");

    for(i = 0; i < 7; i++){
        printf("%.1f\n", vetor_saida[i]);
    }

    // Filtro FIR
    int amostras_entrada[4] = {4, 8, 6, 5};
    float coeficientes[3] = {0.33, 0.33, 0.33};
    float sinal_filtrado[4];


    filtroFir(amostras_entrada, coeficientes, 4, 3, sinal_filtrado);

    printf("Resultado do Filtro FIR\n");

    for(i = 0; i < 4; i++){
        printf("%.1f\n", sinal_filtrado[i]);
    }

    // Filtro IIR

    Coeficientes coeficiente;

    coeficiente.b0 = 0.2929;
    coeficiente.b1 = 0.5858;
    coeficiente.b2 = 0.2929;
    coeficiente.a1 = -0.0000;
    coeficiente.a2 = 0.1716;

    float entrada[8] = { 0.0, 0.5, 0.8, 0.3, -0.2, -0.5, -0.3, 0.1 };
    float saida[8];

    
    filtroIIR(entrada, saida, 8, coeficiente);

    printf("Resultado do Filtro IIR\n");

    for(i = 0; i < 8; i++){
        printf("%.1f\n", saida[i]);
    }

    // Downsampling 
    float entrada_downsample[4] = {1.3, 2.0, 4.3, 3.1};
    int tamanho_entrada = 4;
    int fator = 2;
    int tamanho_saida = (tamanho_entrada + fator - 1) / fator;
    float saida_downsample[tamanho_saida];

    downsample(entrada_downsample, tamanho_entrada, fator, saida_downsample);
    printf("Resultado do Downsampling\n");

    for(i = 0; i < tamanho_saida; i++){
        printf("%.1f\n", saida_downsample[i]);
    }

    // Denoising

    float entrada_denoising[4] = {4.3, 3.0, 1.3, 2.1};
    int tamanho_denoising = 4;
    int janela = 4;
    float saida_denoising[tamanho_denoising];

    denoising(entrada_denoising, tamanho_denoising, janela, saida_denoising);

    printf("Resultado do Denoising\n");

    for(i = 0; i < tamanho_denoising; i++){
        printf("%.1f\n", saida_denoising[i]);
    }


    return 0;
}
// começar o rotinas compressao adaptativa
// gcc -o app main.c bib.c | ./app