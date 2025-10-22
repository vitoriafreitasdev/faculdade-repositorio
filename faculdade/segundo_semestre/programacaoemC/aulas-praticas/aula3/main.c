#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
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
            printf("Reprovado. Continue se esforçando!");
        }


        return 0;
}




