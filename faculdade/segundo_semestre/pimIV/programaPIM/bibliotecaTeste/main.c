

#include <stdio.h>
#include <stdlib.h>
#include "library.h"


int main(){

    printf("%d + %d = %d\n", 4, 5, add(4, 5));
    printf("%d + %d = %d\n", 10, 7, sub(10, 7));
    printf("Deu certo!!");
    

    return 0;
}

// gcc -o app main.c library.c | ./app