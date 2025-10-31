
#include <stdio.h>
#include <stdlib.h>
#include "bib.h"

int main(){
  
    int vetor[7] = {-32700, -15000, -8000, 0, 12000, 25000, 31000};
    float vetor_saida[7];
    int i;
    
    sinais_normalizados(vetor, 7, 32767, vetor_saida);
    printf("depois de chamar a funcao\n");

    for(i = 0; i < 7; i++){
        printf("%.1f\n", vetor_saida[i]);
    }
  
    return 0;
}
/* 
fazer
Decodificação Delta
delta_decode(int16_t *in, size_t n, int16_t *out)
Reconstrói o sinal original.

*/
// gcc -o app main.c bib.c | ./app