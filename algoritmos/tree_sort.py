"""
    Algoritmo de ordenação adaptado de GFG - GeeksForGeeks
    Disponível em: https://www.geeksforgeeks.org/tree-sort/
"""
class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def inserir(raiz, chave):
    if raiz is None:
        return Node(chave)
    if chave < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, chave)
    else:
        raiz.direita = inserir(raiz.direita, chave)
    return raiz

def in_ordem(raiz, resultado):
    if raiz:
        in_ordem(raiz.esquerda, resultado)
        resultado.append(raiz.chave)
        in_ordem(raiz.direita, resultado)

def ordenar(n):
    if not n:
        return []

    raiz = None
    for chave in n:
        raiz = inserir(raiz, chave)

    resultado = []
    in_ordem(raiz, resultado)
    return resultado
