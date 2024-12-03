from typing import List
import random

def cria_grafo(matriz):
    tamanho = len(matriz[0])
    graph = {i * tamanho + j: [] for i in range(len(matriz)) for j in range(len(matriz[0])) if matriz[i][j] == 1}
    rows, cols = len(matriz), len(matriz[0])

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(rows):
        for col in range(cols):
            if matriz[row][col] == 1:
                for dr, dc in dir:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matriz[nr][nc] == 1:
                        graph[row * tamanho + col].append((nr * tamanho + nc))
    
    return graph

def dfs_normal(grafo, inicio, visitados):
    if inicio not in visitados:
        visitados.add(inicio)
        for vizinho in grafo[inicio]:
            dfs_normal(grafo, vizinho, visitados)

def dfs_numbering(grafo, inicio, post, cont):
    print("contagem")
    print(post)
    if post.get(inicio, -1) != -1:  # Verifica se o nó já foi processado
        return
    post[inicio] = cont[0]
    cont[0] += 1
    print(grafo[inicio])
    for vizinho in grafo[inicio]:
        dfs_numbering(grafo, vizinho, post, cont)
    post[inicio] = cont[0]
    cont[0] += 1

def dfs(grafo):
    print('dfs_teste')
    post = {no: -1 for no in grafo}
    componentes = 0
    cont = [0]
    print(post)
    
    for no in grafo:
        print(no)
        if post[no] == -1:
            componentes += 1
            dfs_numbering(grafo, no, post, cont)
            cont[0] -= 1
            post[no] = cont[0]
            

    return post, componentes

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        grafo = cria_grafo(grid)

        if not grafo:  # Caso o grafo já esteja desconectado
            return 0
        
        visitados = set()
        dfs_normal(grafo, random.choice(list(grafo.keys())), visitados)
        post, componentes = dfs(grafo)
        days = 0

        print(componentes)

        while componentes >= 1: 
            # Excluir o nó com o maior valor de pós-visita
            print(grafo)
            print("no removido")
            print(post)
            maior_no = max(post, key=post.get)
            print(maior_no)
            if maior_no in grafo: 
                del grafo[maior_no]
                for no in grafo:
                    grafo[no] = [v for v in grafo[no] if v != maior_no]  # Remover conexões ao nó deletado
            days += 1
            print("chamando verificação")
            print(grafo)
            post, componentes = dfs(grafo)
            print(componentes)

        return days

