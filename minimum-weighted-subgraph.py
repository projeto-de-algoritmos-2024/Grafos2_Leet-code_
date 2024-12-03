import heapq

def dijkstra(grafo, origem):
    distancias = dict()
    heap = [(0, origem)]                           

    while heap:
        distancia_atual, atual = heapq.heappop(heap)

        if not atual in distancias:
            distancias[atual] = distancia_atual
            for vizinho, peso in grafo[atual]:
                distancia = distancia_atual + peso
                if not vizinho in distancias:
                    heapq.heappush(heap, (distancia, vizinho))

    return distancias

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        grafo = {str(no): [] for no in range(n)}
        grafo_reverso = {str(no): [] for no in range(n)}

        for edge in edges:
            no, vizinho, peso = edge
            grafo[str(no)].append((str(vizinho), peso))
            grafo_reverso[str(vizinho)].append((str(no), peso))

        src1_todos = dijkstra(grafo, str(src1))
        src2_todos = dijkstra(grafo, str(src2))
        reverso = dijkstra(grafo_reverso, str(dest))

        peso = float('inf')
        for i in range(n):
            no = str(i)
            if no in src1_todos and no in src2_todos and no in reverso:
                peso = min(peso, src1_todos[no] + src2_todos[no] + reverso[no])

        return int(peso if float(peso) < float('inf') else -1)

