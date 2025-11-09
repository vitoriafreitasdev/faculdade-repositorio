
//bib.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "bib.h"
#include <string.h>

// formula valor_normalizado = valor_original / valor_maximo_absoluto
// Normalizar significa pegar esse vetor e ajustar todos os valores para caber em uma faixa fixa
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
/* FIR = Finite Impulse Response => Ele pega as últimas N amostras e faz média ponderada delas. */
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

//Filtro IIR(biquad)
/* Um filtro IIR (Infinite Impulse Response) usa realimentação (feedback): ele utiliza amostras atuais e anteriores da entrada e amostras anteriores da saída. Formula: y[n] = b0 * x[n] + b1 * x[n−1] + b2 * x[n−2] − a1 * y[n−1] − a2 * y[n−2]
*/
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

/*Downsampling => significa diminuir a taxa de amostragem do sinal.*/
void downsample(float entrada[], int tamanho, int fator, float saida[]){
    int indice_saida = 0;
    int i;

    for(i = 0; i < tamanho; i++) {
        if(i % fator == 0){
            saida[indice_saida] = entrada[i];
            indice_saida++;
        }
    }
}

/*Denoising => Reduzir o ruído do sinal suavizando variações bruscas, mas mantendo a forma do sinal (picos e tendências).*/

void denoising(float entrada[], int tamanho, int janela, float saida[]){
    int metade = janela / 2;
    int i, k;
    for(i = 0; i < tamanho; i++){
        float acumulador = 0;
        int contador = 0;

        for(k = -metade; k <= metade; k++) {
            int indice = i + k;

            if(indice < 0 || indice >= tamanho){
                continue;
            }

            acumulador += entrada[indice];
            contador++;
        }
        saida[i] = acumulador / contador;
    }
}

// Rotinas compressão adaptativa 
/* 
Delta Encoding
A codificação delta é uma técnica de compressão simples onde não armazenamos os valores originais do sinal, mas sim as diferenças entre uma amostra e a anterior.
*/

void codificacao_delta(float entrada[], int tamanho, float saida[]){
    // Primeiro valor é copiado sem alteração
    saida[0] = entrada[0];

    int i;

    // Calcula a diferença das próximas amostras
    for(i = 1; i < tamanho; i++){
        saida[i] = entrada[i] - entrada[i - 1];
    }

}

/* 
decodificação delta
A função recebe um vetor com valores codificados por delta (diferenças) e reconstrói o sinal original somando cada diferença ao valor acumulado anterior.
*/

void decodificacao_delta(float entrada[], int tamanho, float saida[]){
    saida[0] = entrada[0];

    int i;

    for(i = 1; i < tamanho; i++){
        saida[i] = saida[i-1] + entrada[i];
    }

}

/*
RLE Adaptativo
O RLE adaptativo é uma variação do RLE tradicional.
No RLE clássico, comprime sequências de valores iguais consecutivos (ex.: 5 5 5 5 → (5,4)).
No RLE adaptativo, você define um limiar (threshold) para considerar valores "suficientemente próximos", e não apenas idênticos.
*/
void RLEAdaptativo(float entrada[], int tamanho, float threshold, float valores[], int contagens[], int *tamanho_saida) {
    float valor_atual = entrada[0];
    int contador = 1;
    int indice_saida = 0;

    for (int i = 1; i < tamanho; i++) {
        if (fabs(entrada[i] - valor_atual) <= threshold) {
            contador++;
        } else {
            valores[indice_saida] = valor_atual;
            contagens[indice_saida] = contador;
            indice_saida++;

            valor_atual = entrada[i];
            contador = 1;
        }
    }

    // Salva o último grupo
    valores[indice_saida] = valor_atual;
    contagens[indice_saida] = contador;

    *tamanho_saida = indice_saida + 1;
}

//Entropia de Janela (Window Entropy)
/* 
A entropia mede o nível de imprevisibilidade (caos) do sinal dentro de uma janela (um pedaço do vetor).
Em sinais biomédicos ou industriais, isso serve para:
detectar momentos de instabilidade,
diferenciar atividade (sinal variando muito) e repouso (sinal estável),
identificar eventos anormais.

- Quanto maior a entropia, mais variáveis e imprevisíveis são os valores naquela janela.
- Quanto menor a entropia, mais repetitivos e previsíveis são os valores.*/


void entropia_janela(float entrada[], int tamanho, int janela, float saida[]){
    int i, k;

    for(i = 0; i <= tamanho - janela; i++){

        float freq[100] = {0};

        for(k = 0; k < janela; k ++){
            int indice = (int) entrada[i + k];
            freq[indice]++;
        }

        float entropia = 0.0f;

        for(k = 0; k < 100; k++){
            if (freq[k] > 0) {
                float prob = (float)freq[k] / janela;
                entropia += prob * log2(prob);
            }
        }
        // -entropia, pois resultado da entropia fica positivo (como deve ser)
        saida[i] = -entropia;

    }
}

/*
Integridade (Checksum / Verificação de Integridade)
Quando transmitimos ou armazenamos dados (em dispositivos médicos, pesquisa clínica ou indústria farmacêutica), precisamos garantir que o sinal não foi alterado ou corrompido.
A técnica mais simples e bastante usada é o Checksum:
Um checksum calcula um valor numérico (soma ou operação matemática) baseado no conteúdo do vetor.
Se os dados forem modificados, o checksum muda — permitindo identificar erro.
*/

float integridade_checksum(float entrada[], int tamanho){
    float soma = 0.0f;
    int i;
    for(i = 0; i < tamanho; i++){
        soma = soma + entrada[i];
    }
    return soma;
}

// gravar imagem
void gravar_imagem(const Imagens *imagem, const char *nome_arquivo) {

    FILE *arquivo = fopen(nome_arquivo, "wb");
    if (!arquivo) {
        printf("Erro ao abrir arquivo.\n");
        return;
    }

    fwrite(imagem->imagem_nome, sizeof(char), sizeof(imagem->imagem_nome), arquivo);
    fwrite(imagem->imagem_formato, sizeof(char), sizeof(imagem->imagem_formato), arquivo);
    fwrite(&imagem->tamanho, sizeof(unsigned long), 1, arquivo);

    fwrite(imagem->imagem_dados, sizeof(unsigned char), imagem->tamanho, arquivo);

    fclose(arquivo);

    printf("Imagem '%s' salva em '%s'\n", imagem->imagem_nome, nome_arquivo);
}


Imagens* ler_imagem_binaria(const char *nome_arquivo) {

    FILE *arquivo = fopen(nome_arquivo, "rb");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo para leitura.\n");
        return NULL;
    }

    // Aloca a estrutura dinamicamente
    Imagens *imagem = (Imagens *)malloc(sizeof(Imagens));
    if (!imagem) {
        printf("Erro ao alocar memória para a imagem.\n");
        fclose(arquivo);
        return NULL;
    }

    // Lê os metadados (nome, formato e tamanho)
    fread(imagem->imagem_nome, sizeof(char), sizeof(imagem->imagem_nome), arquivo);
    fread(imagem->imagem_formato, sizeof(char), sizeof(imagem->imagem_formato), arquivo);
    fread(&imagem->tamanho, sizeof(unsigned long), 1, arquivo);

    // Aloca memória para os bytes da imagem
    imagem->imagem_dados = (unsigned char *)malloc(imagem->tamanho);
    if (!imagem->imagem_dados) {
        printf("Erro ao alocar memória para os dados da imagem.\n");
        free(imagem);
        fclose(arquivo);
        return NULL;
    }

    // Lê os bytes reais da imagem
    fread(imagem->imagem_dados, sizeof(unsigned char), imagem->tamanho, arquivo);

    fclose(arquivo);

    printf("Imagem '%s.%s' carregada com sucesso (%lu bytes)\n",
           imagem->imagem_nome, imagem->imagem_formato, imagem->tamanho);

    return imagem;  // retorna a struct alocada dinamicamente
}
