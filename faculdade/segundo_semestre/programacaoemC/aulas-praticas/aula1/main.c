// Aula 1
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
    printf("Ol�, mundo!\n")

    float valor1, valor2, valor3, total;
    valor1 = 12.6;
    valor2 = 3.4;
    valor3 = 6.2;
    total = valor1 + valor2 + valor3;
    printf("Total: %.2f \n", total);

    //

    int idade;
    float altura;
    char inicial;

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite sua altura: ");
    scanf("%f", &altura);

    printf("Digite a inicial do seu nome: ");
    scanf(" %c", &inicial);



    printf("\nIdade: %d, Altura: %.2f, Inicial: %c\n ", idade, altura, inicial);


    //

    char name[50];
    int age;

    printf("Digite seu nome: ");
    scanf("%s", name);

    printf("Digite sua idade: ");
    scanf("%d", &age);

    printf("oL�, %s! Voc� tem %d anoa.\n", name, age);

    return 0;
}
