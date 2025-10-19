import random
import time

def linear_search(arr, target):
    """Retorna o índice da primeira ocorrência de target ou -1 se não existir."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

def binary_search(arr_sorted, target):
    """Busca binária iterativa em lista ORDENADA; retorna índice ou -1."""
    lo, hi = 0, len(arr_sorted) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr_sorted[mid] == target:
            return mid
        if arr_sorted[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def main():
    print("=== Roteiro 5: Busca Linear x Busca Binária ===")
    try:
        n = int(input("Tamanho da lista (mínimo 5000): ").strip())
    except ValueError:
        n = 5000
    if n < 5000:
        n = 5000
        print("Ajustando para 5000 (mínimo exigido).")

    # Geramos números inteiros aleatórios num intervalo razoável.
    # Para ter repetições (e realismo), usamos um range menor que n.
    random.seed(42)
    arr = [random.randint(0, n // 2) for _ in range(n)]

    try:
        target = int(input("Valor-alvo (inteiro): ").strip())
    except ValueError:
        # Se o usuário digitar algo inválido, escolhemos um alvo existente para demonstrar
        target = arr[len(arr) // 2]
        print(f"Entrada inválida. Usando valor-alvo existente na lista: {target}")

    # Lista ordenada para a busca binária
    arr_sorted = sorted(arr)

    # Cronometria — 1 execução cada (pode aumentar para maior robustez)
    t0 = time.perf_counter()
    idx_lin = linear_search(arr, target)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    idx_bin = binary_search(arr_sorted, target)
    t3 = time.perf_counter()

    time_linear = t1 - t0
    time_binary = t3 - t2

    # Observação importante: os índices não são comparáveis entre si,
    # pois um é na lista original e o outro é na ORDENADA.
    print("\n--- Resultados ---")
    print(f"Tamanho da lista: {n}")
    print(f"Alvo: {target}")
    print(f"Linear: índice={idx_lin} | tempo={time_linear*1000:.3f} ms")
    print(f"Binária: índice (na lista ORDENADA)={idx_bin} | tempo={time_binary*1000:.3f} ms")

    if (idx_lin == -1) and (idx_bin == -1):
        print("O valor não foi encontrado em nenhuma das duas buscas.")
    else:
        print("Pelo menos uma busca encontrou o valor.")

    # Vencedor (apenas para esta execução)
    vencedor = "Busca Binária" if time_binary < time_linear else "Busca Linear"
    print(f"Método mais rápido neste experimento: {vencedor}")

if __name__ == "__main__":
    main()
