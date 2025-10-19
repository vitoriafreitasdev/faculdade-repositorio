import random
import string
import time
import heapq
from collections import defaultdict

# ------------------------
# Helpers de geração
# ------------------------
def rand_str(k=12, alphabet=string.ascii_letters + string.digits):
    return ''.join(random.choices(alphabet, k=k))

def gen_pairs(n_keys=50_000, seed=42):
    random.seed(seed)
    keys = [rand_str() for _ in range(n_keys)]
    vals = [random.randint(0, 10_000_000) for _ in range(n_keys)]
    return list(zip(keys, vals)), keys

# ------------------------
# Medições de busca
# ------------------------
def build_dict_and_list(pairs):
    d = dict(pairs)
    lt = pairs[:]              # lista de tuplas (chave, valor)
    return d, lt

def lookup_in_list(lt, k):
    # Busca linear na lista de tuplas (k, v)
    for kk, vv in lt:
        if kk == k:
            return vv
    return None

def measure_lookups(d, lt, keys_to_test):
    t0 = time.perf_counter()
    hit_d = 0
    for k in keys_to_test:
        if k in d:  # O(1) médio
            _ = d[k]
            hit_d += 1
    t_dict = time.perf_counter() - t0

    t1 = time.perf_counter()
    hit_l = 0
    for k in keys_to_test:
        v = lookup_in_list(lt, k)  # O(n) por consulta
        if v is not None:
            hit_l += 1
    t_list = time.perf_counter() - t1
    return t_dict, hit_d, t_list, hit_l

# ------------------------
# Experimentos com heap
# ------------------------
def measure_heap_ops(n_init=20_000, n_pops=5_000, seed=123):
    random.seed(seed)
    data = [random.randint(0, 10_000_000) for _ in range(n_init)]
    t0 = time.perf_counter()
    heapq.heapify(data)              # O(n)
    t_heapify = time.perf_counter() - t0

    t1 = time.perf_counter()
    popped_sum = 0
    for _ in range(n_pops):
        popped_sum += heapq.heappop(data)  # O(log n) por pop
    t_pops = time.perf_counter() - t1
    return t_heapify, t_pops, popped_sum, len(data)

# ------------------------
# Main
# ------------------------
def main():
    print("=== Roteiro 6: Hash Tables (dict) x Lista de Tuplas + Heap (heapq) ===")
    pairs, keys = gen_pairs(n_keys=50_000, seed=2025)
    d, lt = build_dict_and_list(pairs)

    # 1000 chaves para teste: metade existentes, metade ausentes
    present = random.sample(keys, k=500)
    absent  = [rand_str() for _ in range(500)]
    keys_to_test = present + absent
    random.shuffle(keys_to_test)

    # Medir buscas
    t_dict, hit_d, t_list, hit_l = measure_lookups(d, lt, keys_to_test)

    # Heap: 20k itens + 5k pops
    t_heapify, t_pops, popped_sum, remaining = measure_heap_ops(
        n_init=20_000, n_pops=5_000, seed=77
    )

    # Resumo
    print("\n--- Resultados de Busca ---")
    print(f"Total pares inseridos: {len(pairs):,}")
    print(f"Consultas: {len(keys_to_test)} (presentes={len(present)}, ausentes={len(absent)})")
    print(f"Dict:   hits={hit_d}/{len(keys_to_test)}  | tempo={t_dict*1000:.2f} ms")
    print(f"Lista:  hits={hit_l}/{len(keys_to_test)}  | tempo={t_list*1000:.2f} ms")
    winner = "dict (hash table)" if t_dict < t_list else "lista (inesperado)"
    print(f"Mais rápido neste experimento: {winner}")

    print("\n--- Resultados de Heap (mín-heap/heapq) ---")
    print(f"Heapify de 20.000: {t_heapify*1000:.2f} ms")
    print(f"5.000 heappop():   {t_pops*1000:.2f} ms")
    print(f"Itens restantes no heap: {remaining:,}")
    # popped_sum evita que o Python elimine o loop (efeito otimização)
    print(f"Soma dos elementos removidos (sanity check): {popped_sum}")

if __name__ == "__main__":
    main()
