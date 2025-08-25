// aula 3
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
        setlocale(LC_ALL, "Portuguese");

        int idade;
        printf("Digite sua idade: ");
        scanf("%d", &idade);

        if(idade >= 18){
            printf("Voc� � maior de idade.\n");
        }

        //

        int numero;
        printf("Digite um numero: ");
        scanf("%d", &numero);

        if(numero % 2 == 0){
            printf("Par");
        } else {
            printf("Impar");
        }


        //

        int senhaDigitada;
        int senhaCorreta = 1234;

        printf("\nDigite a senha: ");
        scanf("%d", &senhaDigitada);

        if(senhaDigitada == senhaCorreta){
            printf("Senha permitida.\n");
        } else {
            printf("Senha incorreta! tente novamente.\n");
        }

        //

        int nota;

        printf("Digite a nota (0 a 10): ");
        scanf("%d", &nota);

        if (nota >= 7){
            printf("Aprovado.\n");
        } else if (nota >= 5){
            printf("Em recupera��o.\n");
        } else {
            printf("Reprovado.\n");
        }

        // desafio


        char name[50];
        int age;
        float n1;
        float n2;
        float n3;
        float average;

        printf("Coloque seu nome: ");
        scanf("%s", &name);

        printf("Coloque sua idade: ");
        scanf("%d", &age);

        printf("Coloque sua primeira nota: ");
        scanf("%f", &n1);

        printf("Coloque sua segunda nota: ");
        scanf("%f", &n2);

        printf("Coloque sua terceira nota: ");
        scanf("%f", &n2);

        average = (n1 + n2 + n3) / 3;

        if (average >= 9){
            printf("Aprovado com excelente desempenho!");
        } else if (average >= 7){
            printf("Aprovado, mas ainda pode melhorar.");
        } else {
            printf("Reprovado. Continue se esfor�ando!");
        }


        return 0;
}
