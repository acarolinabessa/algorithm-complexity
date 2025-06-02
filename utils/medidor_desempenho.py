import time
import tracemalloc

def medir_desempenho(funcao, dados):
    tracemalloc.start()
    inicio = time.perf_counter()
    funcao(dados)
    fim = time.perf_counter()
    memoria = tracemalloc.get_traced_memory()[1] / 1024  # em KB
    tracemalloc.stop()
    return fim - inicio, memoria