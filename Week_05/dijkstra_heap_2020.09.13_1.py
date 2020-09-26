import time
import heapq

def dijkstra_1(G, start):     ### dijkstra算法
    '''
    Dijkstra 要准备的4样东西：
        PriorityQueue 用来辅助执行算法, 
        visited 用来避免重复访问, 
        distance 哈希表用来保存最短路径结果（距离），
        path 表用来保存最短路径结果（路径）
    '''
    dis = dict((key, float("inf")) for key in G)    # start到每个点的距离，初始化为无穷大
    dis[start] = 0                                  # 初始时，把start点的最短距离设为0
    visited = set()                                 # 是否访问过
    # 堆优化
    pq = []                                         # Priority Queue，一个辅助优先队列，用来存放排序后的值
    heapq.heappush(pq, (dis[start], start))         # 将当前节点的最短路径 推入pq，准备开始算法过程
    
    path = dict((key, [start]) for key in G)        # 记录到每个点的路径
    # 算法过程
    while len(pq) > 0:
        v_dis, v = heapq.heappop(pq)                # 未访问点中距离最小的点和对应的距离
        if v in visited:
            continue
        visited.add(v)
        p = path[v].copy()                          # 到v的最短路径
        for node in G[v]:                           # 与v直接相连的点
            new_dis = dis[v] + float(G[v][node])    # 到相邻点的距离等于start点到v点的距离加上v点到node点的距离
            if new_dis < dis[node] and (node not in visited):    # 如果与v直接相连的node通过v到src的距离小于dis中对应的node的值, 则用小的值替换
                dis[node] = new_dis                 # 更新点的距离
                heapq.heappush(pq, (dis[node], node))   # 在dis中更新了最短距离，然后把新的 距离+点 推入优先队列
                temp = p.copy()
                temp.append(node)                   # 更新node的路径zxm,zx
                path[node] = temp                   # 将新路径赋值给temp
                
    return dis, path

def dijkstra(Graph, start):
    distance = {k: float('inf') for k in Graph}
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (distance[start], start))
    visited = set()
    path = {k:[start] for k in Graph}
    # Algorithm
    while pq: 
        dis, node = heapq.heappop(pq)
        if node in visited: continue                # 注意点1：此举是为了防止重复访问更长的路径
        visited.add(node)
        for adjacency in Graph[node]:
            new_dis = dis + Graph[node][adjacency]
            if new_dis < distance[adjacency] and (adjacency not in visited): # 更新路径
                distance[adjacency] = new_dis
                heapq.heappush(pq, (new_dis, adjacency))
                path[adjacency] = path[node] + [adjacency]
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
    distance, path = dijkstra(G, "A")
    distance1, path1 = dijkstra_1(G, "A")
    # distance, path = dijkstra(graph, "S")
    print(distance, path)
    print(distance1, path1)