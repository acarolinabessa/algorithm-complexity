from utils.leitor import ler_arquivo
from utils.gerador_dados import gerar_melhor_caso, gerar_pior_caso, gerar_casos_aleatorios
from utils.medidor_desempenho import medir_desempenho
from datetime import datetime
import csv
import os

def salvar_resultado(timestamp, algoritmo, n, caso, tempo, memoria):
    os.makedirs("resultados", exist_ok=True)
    with open("resultados/resultados.csv", mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, algoritmo, n, caso, f"{tempo:.6f}", f"{memoria:.2f}"])

def main():
    n, algoritmo = ler_arquivo("entrada.txt")
    algoritmos = {
        "bubblesort": "bubble_sort",
        "treesort": "tree_sort",
        "shellsort": "shell_sort"
    }

    modulo_alg = __import__(f"algoritmos.{algoritmos[algoritmo]}", fromlist=['ordenar'])
    ordenar = getattr(modulo_alg, 'ordenar')

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    # Melhor caso
    print(f"[{timestamp}] Iniciando execução do {algoritmo.upper()} com n={n} - MELHOR CASO")
    dados = gerar_melhor_caso(n)
    tempo, memoria = medir_desempenho(ordenar, dados)
    salvar_resultado(timestamp, algoritmo, n, "melhor", tempo, memoria)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Finalizou MELHOR CASO")

    # Pior caso
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando execução do {algoritmo.upper()} com n={n} - PIOR CASO")
    dados = gerar_pior_caso(n)
    tempo, memoria = medir_desempenho(ordenar, dados)
    salvar_resultado(timestamp, algoritmo, n, "pior", tempo, memoria)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Finalizou PIOR CASO")

    # Casos médios (5 execuções aleatórias)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando execução do {algoritmo.upper()} com n={n} - MÉDIO (5 execuções)")
    tempos, mems = [], []
    for i in range(5):
        dados = gerar_casos_aleatorios(n)
        tempo, memoria = medir_desempenho(ordenar, dados)
        tempos.append(tempo)
        mems.append(memoria)
        print(f"  → Execução {i+1}/5 concluída")

    salvar_resultado(timestamp, algoritmo, n, "medio", sum(tempos)/5, sum(mems)/5)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Finalizou MÉDIO")

if __name__ == "__main__":
    main()
