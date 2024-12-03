import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:  

        def manhattan_distancia(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def prim(points):
            n = len(points)
            mst = []
            visitado = set()
            min_heap = []

            visitado.add(0)
            for i in range(1, n):
                dist = manhattan_distancia(points[0], points[i])
                heapq.heappush(min_heap, (dist, 0, i))

            while len(visitado) < n:
                weight, frm, to = heapq.heappop(min_heap)

                if to in visitado:
                    continue

                mst.append((points[frm], points[to], weight))
                visitado.add(to)

                for i in range(n):
                    if i not in visitado:
                        dist = manhattan_distancia(points[to], points[i])
                        heapq.heappush(min_heap, (dist, to, i))

            return mst

        mst = prim(points)
        soma = sum(w for _, _, w in mst)
        return soma
