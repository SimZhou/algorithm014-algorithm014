import time, sys
import heapq

def dijkstra(Graph, start):
    '''准备3样东西：pq, distance, visited；如果需要打印路径则还需一个path'''
    pq = []
    heapq.heappush(pq, (0, start))
    distance = {k: sys.maxsize for k in Graph}
    distance[start] = 0
    visited = set()
    path = {k: [start] for k in Graph}

    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node)
        for adjnode in Graph[node]:
            new_dist = distance[node] + Graph[node][adjnode]
            if new_dist < distance[adjnode] and (adjnode not in visited):
                distance[adjnode] = new_dist
                heapq.heappush(pq, (new_dist, adjnode))
                path[adjnode] = path[node] + [adjnode]
    return distance, path

if __name__ == '__main__':
    G = {
            "A":{"B":5, "C":1},
            "B":{"A":5, "C":2, "D":1},
            "C":{"A":1, "B":2, "D":4, "E":8},
            "D":{"B":1, "C":4, "E":3, "F":6},
            "E":{"C":8, "D":3},
            "F":{"D":6}
        }
    G1 = {
        "S": {"A": 7, "B": 2, "C": 3},
        "A": {"S": 7, "B": 3, "D": 4},
        "B": {"S": 2, "A": 3, "D": 4, "H":1},
        "C": {"S": 3, "L": 2},
        "D": {"A": 4, "B": 4, "F": 5},
        "E": {"G": 2, "K": 5},
        "F": {"D": 5, "H": 3},
        "G": {"E": 2, "H": 2},
        "H": {"B": 1, "F": 3, "G": 2},
        "I": {"J": 6, "K": 4, "L": 4},
        "J": {"I": 6, "K": 4, "L": 4},
        "K": {"E": 5, "I": 4, "J": 4},
        "L": {"C": 2, "I": 4, "J": 4}
    }
    distance, path = dijkstra(G1, "A")
    # distance1, path1 = dijkstra_1(G, "A")
    # distance, path = dijkstra(graph, "S")
    print(distance, path)
    # print(distance1, path1)