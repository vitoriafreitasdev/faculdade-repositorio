#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
int calcula_quadrado(int num) {
        return num * num;
}

// exemplo 2

void modifReferencia(int *x){
        printf("Dentro da fun��o, antes da modifica��o: *ptr = %d\n", *x);
        *x = 100;
        printf("Dentro da fun��o, depois da modifica��o: *ptr = %d\n", *x);
}

// exemplo 3

    double resultado;

    void calculaquadrado(double num){
        resultado = num * num;
    }

    double calculasoma(double n1, double n2){
        double r;
        r = n1 + n2;
        return r;
    }

    // desafio
    int contar_caracteres(char nome[]);

int main()
{
    setlocale(LC_ALL, "Portuguese");

    int num = 10;

    void mostrar_quadrado(int num){
        printf("%d\n", num * num);
    }

    mostrar_quadrado(num);

    int n1 = 4;

    int quad = calcula_quadrado(n1);

    printf("%d\n", quad);

    // exemplo 2

    int valor = 10;

    printf("Antes da chamada da fun��o: valor = %d\n", valor);

    modifReferencia(&valor);

    printf("Depois da chamada da fun��o: valor = %d\n", valor);

    // exemplo 3

    int a = 2, b = 3;

    resultado = calculasoma(a, b);
    printf("%.2lf\n", resultado);

    calculaquadrado(resultado);
    printf("%.2lf\n", resultado);

    calculaquadrado(resultado);
    printf("%.2lf\n", resultado);


    // desafio

    char nome[50];
    printf("Digite seu nome: ");
    fgets(nome, sizeof(nome), stdin); // le nome com espa�os

    int total = contar_caracteres(nome);
    printf("O nome possui %d caracteres.\n", total);


    return 0;
}

    // desafio

    int contar_caracteres(char nome[]) {

        int i = 0;
        // conta espa�o entre nome e sobrenome
        while(nome[i] != '\0'){
            i++;
        }
        return i;

    }
