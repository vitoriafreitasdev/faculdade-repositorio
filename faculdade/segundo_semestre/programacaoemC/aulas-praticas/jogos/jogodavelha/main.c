
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define LIN 3
#define COL 3

// Tabuleiro armazenado em um array bidimensional
void inicializa_tabuleiro(char t[LIN][COL]) {
    int pos = 1;
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            t[i][j] = '0' + pos++; // '1'..'9' para guiar o usuário
        }
    }
}

void imprime_tabuleiro(const char t[LIN][COL]) {
    system("cls||clear"); // limpa tela no Windows/Linux
    printf("\n===== JOGO DA VELHA =====\n\n");
    for (int i = 0; i < LIN; i++) {
        for (int j = 0; j < COL; j++) {
            printf(" %c ", t[i][j]);
            if (j < COL - 1) printf("|");
        }
        if (i < LIN - 1) printf("\n---+---+---\n");
    }
    printf("\n\n");
}

// Converte posição 1..9 para índices (i, j)
int pos_to_ij(int pos, int *pi, int *pj) {
    if (pos < 1 || pos > 9) return 0;
    pos--;              // 0..8
    *pi = pos / 3;      // linha
    *pj = pos % 3;      // coluna
    return 1;
}

// Verifica se há vencedor; retorna 'X', 'O' ou '\0' se ninguém
char vencedor(const char t[LIN][COL]) {
    // Linhas e colunas
    for (int i = 0; i < 3; i++) {
        if (t[i][0] == t[i][1] && t[i][1] == t[i][2]) return t[i][0];
        if (t[0][i] == t[1][i] && t[1][i] == t[2][i]) return t[0][i];
    }
    // Diagonais
    if (t[0][0] == t[1][1] && t[1][1] == t[2][2]) return t[0][0];
    if (t[0][2] == t[1][1] && t[1][1] == t[2][0]) return t[0][2];
    return '\0';
}

int tabuleiro_cheio(const char t[LIN][COL]) {
    for (int i = 0; i < LIN; i++)
        for (int j = 0; j < COL; j++)
            if (t[i][j] >= '1' && t[i][j] <= '9') // ainda livre
                return 0;
    return 1;
}

// Tenta jogar; retorna 1 se ok, 0 se posição inválida/ocupada
int joga(char t[LIN][COL], int pos, char jogador) {
    int i, j;
    if (!pos_to_ij(pos, &i, &j)) return 0;
    if (t[i][j] == 'X' || t[i][j] == 'O') return 0;
    t[i][j] = jogador;
    return 1;
}

// Lê uma jogada segura do usuário
int ler_jogada() {
    char buf[64];
    while (1) {
        if (!fgets(buf, sizeof(buf), stdin)) return -1;
        int p = -1;
        // aceita um único número na entrada
        if (sscanf(buf, "%d", &p) == 1) return p;
        printf("Entrada invalida. Digite um numero de 1 a 9: ");
    }
}

int main(void) {
    char tab[LIN][COL];
    char jog = 'X';
    int pos;
    inicializa_tabuleiro(tab);

    while (1) {
        imprime_tabuleiro(tab);
        printf("Vez do jogador %c. Escolha uma posicao (1-9): ", jog);
        pos = ler_jogada();
        if (pos == -1) {
            printf("\nEntrada encerrada.\n");
            break;
        }
        if (!joga(tab, pos, jog)) {
            printf("Posicao invalida/ocupada. Pressione ENTER e tente outra...\n");
            getchar();
            continue;
        }

        char v = vencedor(tab);
        if (v == 'X' || v == 'O') {
            imprime_tabuleiro(tab);
            printf("Jogador %c venceu! Parabens!\n", v);
            break;
        }

        if (tabuleiro_cheio(tab)) {
            imprime_tabuleiro(tab);
            printf("Deu velha! Empate.\n");
            break;
        }

        jog = (jog == 'X') ? 'O' : 'X';
    }

    printf("\nFim de jogo. Pressione ENTER para sair...");
    getchar();
    return 0;
}