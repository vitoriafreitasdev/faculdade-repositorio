
// bib.h
#ifndef BIB_H
#define BIB_H

// struct para os coefiecientes
typedef struct 
{
    float b0, b1, b2;
    float a1, a2;
} Coeficientes;
// struct para as imagens
typedef struct 
{
    char imagem_nome[50];
    char imagem_formato[10];
    unsigned long tamanho;
    unsigned char *imagem_dados;
} Imagens;


void sinais_normalizados(int vetor[], int tamanho, int valor_maximo_absoluto, float vetor_saida[]);
void filtroFir(int amostras_entrada[], float coeficientes[], int tamanho_entrada, int tamanho_coeficientes, float sinal_filtrado[]);
void filtroIIR(float entrada[], float saida[], int tamanho, Coeficientes coeficientes);
void downsample(float entrada[], int tamanho, int fator, float saida[]);
void denoising(float entrada[], int tamanho, int janela, float saida[]);
void codificacao_delta(float entrada[], int tamanho, float saida[]);
void decodificacao_delta(float entrada[], int tamanho, float saida[]);
void RLEAdaptativo(float entrada[], int tamanho, float threshold, float valores[],int contagens[], int *tamanho_saida);
void entropia_janela(float entrada[], int tamanho, int janela, float saida[]);
float integridade_checksum(float entrada[], int tamanho);
void gravar_imagem(const Imagens *imagem, const char *nome_arquivo);

#endif