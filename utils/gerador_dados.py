import random

def gerar_melhor_caso(n):
    return list(range(n))

def gerar_pior_caso(n):
    return list(range(n, 0, -1))

def gerar_casos_aleatorios(n):
    return random.sample(range(n * 10), n)
