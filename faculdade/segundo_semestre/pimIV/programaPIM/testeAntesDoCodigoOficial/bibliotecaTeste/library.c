
#include <stdio.h>

// exporta as funções da DLL corretamente no Windows
__declspec(dllexport) int add(int x, int y) {
    printf("Add function\n");
    return x + y;
}

__declspec(dllexport) int sub(int x, int y) {
    printf("Sub function\n");
    return x - y;
}

