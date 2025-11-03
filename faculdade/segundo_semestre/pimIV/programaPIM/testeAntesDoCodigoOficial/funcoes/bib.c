
//bib.c
#include <stdio.h>
#include <stdlib.h>

#include "bib.h"

// formula valor_normalizado = valor_original / valor_maximo_absoluto
// Pré-processamentoz
void sinais_normalizados(int vetor[], int tamanho, int valor_maximo_absoluto, float vetor_saida[]){
    if (valor_maximo_absoluto == 0) {
        printf("Erro: valor_maximo_absoluto não pode ser zero.\n");
        return;
    }

    int i;
    for(i = 0; i < tamanho; i++){
        float valor = (float)vetor[i] / valor_maximo_absoluto;
        vetor_saida[i] = valor;  
    }
    
}

// Filtro FIR

/* FIR = Finite Impulse Response
-Ele pega as últimas N amostras e faz média ponderada delas.
Ela vai receber: 
Um vetor de amostras de entrada (ex.: ECG normalizado), exemplo: [4, 8, 6, 5]
Um vetor de coeficientes do filtro FIR (pesos aplicados às amostras), exemplo: [0.33, 0.33, 0.33]
tamanho do sinal (quantas amostras existem) - É o tamanho do vetor de amostras de entrada, ou seja, quantas amostras do sinal você tem para filtrar.
número de coeficientes (ordem do filtro) - É o tamanho do vetor de coeficientes, ou seja, quantos valores (pesos) o filtro FIR vai usar em cada cálculo.
Um vetor de saída onde você vai guardar o sinal filtrado */
void filtroFir(int amostras_entrada[], float coeficientes[], int tamanho_entrada, int tamanho_coeficientes, float sinal_filtrado[]){
    float acumulador = 0.0f;
    int i, k;

    for(i = 0; i < tamanho_entrada; i++){
        acumulador = 0;

        for(k = 0; k < tamanho_coeficientes; k++){
            
            if(i - k >=0) {
                acumulador += amostras_entrada[i - k] * coeficientes[k];
            } 

        }
        
        sinal_filtrado[i] = acumulador;
       
    }

}


void filtroIIR(float entrada[], float saida[], int tamanho, Coeficientes coeficientes){

    float x1 = 0.0f;
    float x2 = 0.0f;
    float y1 = 0.0f;
    float y2 = 0.0f;
    int i;
    for(i = 0; i < tamanho; i++){
        float x0 = entrada[i];
        float y0 = (coeficientes.b0 * x0) + (coeficientes.b1 * x1) + (coeficientes.b2 * x2)- (coeficientes.a1 * y1) - (coeficientes.a2 * y2);
        saida[i] = y0;

        x2 = x1;
        x1 = x0;
        y2 = y1;
        y1 = y0;

    }


}

//Filtro IIR(biquad)
/* Um filtro IIR (Infinite Impulse Response) usa realimentação (feedback): ele utiliza amostras atuais e anteriores da entrada e amostras anteriores da saída. Formula: y[n] = b0 * x[n] + b1 * x[n−1] + b2 * x[n−2] − a1 * y[n−1] − a2 * y[n−2]
A função deve receber:
vetor de entrada
vetor de saída
coeficientes b0, b1, b2, a1, a2
tamanho do sinal
Manter estado entre iterações (x[n−1], x[n−2], y[n−1], y[n−2])
Para cada amostra:
aplica a equação
grava o resultado no vetor de saída
atualiza os valores anteriores
*/