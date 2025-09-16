// Aula 1
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
    // primeira atividade

    printf("Ola, mundo!\n");


    // segunda atividade

    float valor1, valor2, valor3, total;
    valor1 = 12.6;
    valor2 = 3.4;
    valor3 = 6.2;
    total = valor1 + valor2 + valor3;
    printf("Total: %.2f \n", total);

    // terceira atividade

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

    // variáveis
    char name[50];
    char email[50];
    int age;

    // leitura de dados
    printf("Digite seu nome: ");
    scanf("%s", &name);

    printf("Digite sua idade: ");
    scanf("%d", &age);

    printf("Digite seu e-mail: ");
    scanf("%s", &email);

    // mostrando os dados
    printf("Ola, %s! Voce tem %d anos, seu e-mail: %s\n", name, age, email);

    return 0;

}
