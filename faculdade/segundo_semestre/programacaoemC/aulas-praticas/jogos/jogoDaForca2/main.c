#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <locale.h>

#ifdef _WIN32
  #define CLEAR() system("cls")
#else
  #define CLEAR() system("clear")
#endif

#define MAX_PALAVRAS   256
#define MAX_TAM        64
#define MAX_TENTATIVAS 6

// ------- Utilidades -------
static void chomp(char *s) {
    size_t n = strlen(s);
    if (n && (s[n-1] == '\n' || s[n-1] == '\r')) s[n-1] = '\0';
}

static char to_upper_ascii(char c) {
    if (c >= 'a' && c <= 'z') return (char)(c - 'a' + 'A');
    return c;
}

static void str_upper_ascii(char *s) {
    for (; *s; ++s) *s = to_upper_ascii(*s);
}

static int eh_letra_ascii(char c) {
    c = to_upper_ascii(c);
    return (c >= 'A' && c <= 'Z');
}

// ------- Banco de palavras -------
static char banco[MAX_PALAVRAS][MAX_TAM];
static int usada[MAX_PALAVRAS];
static int n_palavras = 0, usadas = 0;

static void inserir_palavra(const char *p) {
    if (!p || !*p) return;
    if (n_palavras >= MAX_PALAVRAS) return;
    strncpy(banco[n_palavras], p, MAX_TAM - 1);
    banco[n_palavras][MAX_TAM - 1] = '\0';
    // armazenar internamente em maiúsculas
    str_upper_ascii(banco[n_palavras]);
    n_palavras++;
}

static void carregar_banco(const char *arquivo) {
    FILE *f = fopen(arquivo, "r");
    if (!f) {
        // fallback inicial
        inserir_palavra("COMPUTADOR");
        inserir_palavra("ALGORITMO");
        inserir_palavra("SISTEMA");
        inserir_palavra("PROGRAMACAO");
        inserir_palavra("MICROCONTROLADOR");
        inserir_palavra("RASPBERRY");
        return;
    }
    char linha[256];
    while (fgets(linha, sizeof(linha), f)) {
        chomp(linha);
        // ignora linhas vazias
        if (linha[0] == '\0') continue;
        // recorta para MAX_TAM
        linha[MAX_TAM-1] = '\0';
        inserir_palavra(linha);
    }
    fclose(f);
    if (n_palavras == 0) { // garante que tenha algo
        inserir_palavra("FORCA");
    }
}

static void salvar_banco(const char *arquivo) {
    FILE *f = fopen(arquivo, "w");
    if (!f) return;
    for (int i = 0; i < n_palavras; i++) {
        fprintf(f, "%s\n", banco[i]);
    }
    fclose(f);
}

// ------- Desenho da forca -------
static void desenha_forca(int erros) {
    // MAX_TENTATIVAS = 6  →  0..6
    const char *stages[7] = {
        "  _______\n"
        " |/      |\n"
        " |       \n"
        " |       \n"
        " |       \n"
        " |       \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |       \n"
        " |       \n"
        " |       \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |       |\n"
        " |       |\n"
        " |       \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |      \\|\n"
        " |       |\n"
        " |       \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |      \\|/\n"
        " |       |\n"
        " |       \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |      \\|/\n"
        " |       |\n"
        " |      / \n"
        "_|___    \n",

        "  _______\n"
        " |/      |\n"
        " |      (_)\n"
        " |      \\|/\n"
        " |       |\n"
        " |      / \\\n"
        "_|___    \n"
    };
    if (erros < 0) erros = 0;
    if (erros > MAX_TENTATIVAS) erros = MAX_TENTATIVAS;
    printf("%s\n", stages[erros]);
}

// ------- Jogo -------
static void mostrar_palavra(const char *palavra, const int vistos[26]) {
    // Mostra letras acertadas e oculta as restantes
    for (size_t i = 0; palavra[i]; ++i) {
        char c = to_upper_ascii(palavra[i]);
        if (!eh_letra_ascii(c)) { // mostra pontuação/espaços
            printf("%c ", palavra[i]);
        } else {
            int idx = c - 'A';
            if (vistos[idx]) printf("%c ", c);
            else printf("_ ");
        }
    }
    printf("\n");
}

static int palavra_completa(const char *palavra, const int vistos[26]) {
    for (size_t i = 0; palavra[i]; ++i) {
        char c = to_upper_ascii(palavra[i]);
        if (eh_letra_ascii(c)) {
            if (!vistos[c - 'A']) return 0;
        }
    }
    return 1;
}

static void mostrar_usadas(const int tentadas[26]) {
    printf("Letras usadas: ");
    int printed = 0;
    for (int i = 0; i < 26; i++) {
        if (tentadas[i]) {
            printf("%c ", 'A' + i);
            printed = 1;
        }
    }
    if (!printed) printf("(nenhuma)");
    printf("\n");
}

static char ler_letra() {
    char buffer[128];
    while (1) {
        if (!fgets(buffer, sizeof(buffer), stdin)) return '\0';
        // pega o primeiro caractere alfabético
        for (int i = 0; buffer[i]; ++i) {
            if (isalpha((unsigned char)buffer[i])) {
                return to_upper_ascii(buffer[i]);
            }
        }
        printf("Digite uma letra valida: ");
    }
}

static void jogar_uma_partida() {
    int idx;
	
	if (n_palavras <= 0) {
        printf("Nenhuma palavra no banco.\n");
        return;
    }

    char nome[MAX_TAM];
    printf("Digite seu nome: ");
    if (!fgets(nome, sizeof(nome), stdin)) return;
    chomp(nome);
    if (nome[0] == '\0') strcpy(nome, "Jogador");

    // escolha aleatória
	if (usadas < n_palavras) {
		do { 
		idx = rand() % n_palavras;
		}while (usada[idx]);
		
		usada[idx] = 1;
		usadas++;
	} else {
		// reset quando varreu todas
		memset(usada, 0, sizeof(usada));
		usadas = 0;
		idx = rand() % n_palavras; // começa novo ciclo
		usada[idx] = 1; usadas++;
	}
	const char *palavra = banco[idx];

    int acertadas[26] = {0};
    int tentadas[26]  = {0};
    int erros = 0;

    while (1) {
        CLEAR();
        printf("===== JOGO DA FORCA =====\n");
        desenha_forca(erros);
        mostrar_palavra(palavra, acertadas);
        mostrar_usadas(tentadas);
        printf("Tentativas restantes: %d\n\n", MAX_TENTATIVAS - erros);

        if (palavra_completa(palavra, acertadas)) {
            printf("Parabens, %s! Voce GANHOU! A palavra era: %s\n", nome, palavra);
            break;
        }
        if (erros >= MAX_TENTATIVAS) {
            printf("Que pena, %s... Voce PERDEU. A palavra era: %s\n", nome, palavra);
            break;
        }

        printf("Digite uma letra: ");
        char chute = ler_letra();
        if (chute == '\0') {
            printf("\nEntrada encerrada.\n");
            break;
        }

        if (!eh_letra_ascii(chute)) {
            printf("Use letras A-Z. Pressione ENTER para continuar...");
            getchar();
            continue;
        }

        int id = chute - 'A';
        if (tentadas[id]) {
            printf("Voce ja tentou a letra '%c'. Pressione ENTER...", chute);
            getchar();
            continue;
        }
        tentadas[id] = 1;

        // verifica acerto
        int acerto = 0;
        for (size_t i = 0; palavra[i]; ++i) {
            char c = to_upper_ascii(palavra[i]);
            if (eh_letra_ascii(c) && c == chute) {
                acertadas[id] = 1;
                acerto = 1;
            }
        }
        if (!acerto) {
            erros++;
        }
    }

    printf("\nPressione ENTER para voltar ao menu...");
    getchar();
}

// ------- Menu -------
static void menu_adicionar_palavra() {
    char nova[MAX_TAM];
    printf("Digite a nova palavra (ate %d caracteres). Evite acentos: ", MAX_TAM-1);
    if (!fgets(nova, sizeof(nova), stdin)) return;
    chomp(nova);
    if (nova[0] == '\0') {
        printf("Palavra vazia. Cancelado.\n");
        printf("Pressione ENTER...");
        getchar();
        return;
    }
    inserir_palavra(nova);
    salvar_banco("palavras.txt");
    printf("OK! Palavra '%s' adicionada.\n", banco[n_palavras-1]);
    printf("Total no banco: %d\n", n_palavras);
    printf("Pressione ENTER...");
    getchar();
}

static void menu_listar_palavras() {
    printf("=== Lista de Palavras (%d) ===\n", n_palavras);
    for (int i = 0; i < n_palavras; i++) {
        printf("%3d) %s\n", i+1, banco[i]);
    }
    printf("\nPressione ENTER...");
    getchar();
}

int main(void) {
    setlocale(LC_ALL, ""); // melhor suporte a console local (ainda assim, prefira sem acentos)
    srand((unsigned)time(NULL));
    carregar_banco("palavras.txt");

    while (1) {
        CLEAR();
        printf("======== FORCA (Console) ========\n");
        printf("1) Jogar\n");
        printf("2) Adicionar nova palavra\n");
        printf("3) Listar palavras\n");
        printf("4) Sair\n");
        printf("Escolha: ");
        char op[16];
        if (!fgets(op, sizeof(op), stdin)) break;
        int c = atoi(op);
        switch (c) {
            case 1: jogar_uma_partida(); break;
            case 2: menu_adicionar_palavra(); break;
            case 3: menu_listar_palavras(); break;
            case 4: salvar_banco("palavras.txt"); return 0;
            default:
                printf("Opcao invalida. Pressione ENTER...");
                getchar();
        }
    }
    salvar_banco("palavras.txt");
    return 0;
}