
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

    return 0;
}
// fazer o filtro Notch
// gcc -o app main.c bib.c | ./app