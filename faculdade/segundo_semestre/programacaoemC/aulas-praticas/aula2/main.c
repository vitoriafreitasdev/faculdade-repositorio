// aula 2
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");

    int a = 10, b = 3;

    printf("Soma: %d\n", a + b);
    printf("Subtra��o: %d\n", a - b);
    printf("Multiplica��o: %d\n", a * b);
    printf("Divis�o: %d\n", a / b);
    printf("Resto da divis�o: %d\n", a % b);

    //

    int x = 5;

    x += 3;
    printf("Resultado de x += 3: %d\n", x);

    x *= 2;
    printf("Resultado de x *= 2: %d\n", x);

    //

    int idade = 18;

    printf("Idade igual a 18? %d\n", idade == 18);
    printf("Idade maior que 17 %d\n", idade > 17);
    printf("Idade diferente de 20? %d\n", idade != 20);

    //
    int A = 5, B = 10;

    printf("a > 0 E b > 0: %d\n",(A > 0) && (B > 0));
    printf("a > 0 OU b < 0: %d\n", (A > 0) || (B < 0));
    printf("N�O (a > b): %d\n", !(A > B));

    //

    char name[50];
    int age;
    float n1, n2, media;

    printf("Digite seu nome: ");
    scanf(" %[^\n]", &name);

    printf("Digite sua idade: ");
    scanf("%d", &age);

    printf("Digite duas notas: ");
    scanf("%f %f", &n1, &n2);

    media = (n1 + n2 ) / 2;

    printf("\Ol�, %s!\n", name);
    printf("M�dia: %.2f\n", media);
    printf("M�dia >= 7? %d\n", media >= 7);
    printf("Idade < 18? %d\n", age < 18);

    return 0;

}
