# 有 N 件物品和一个容量为 V 的背包。
# 第 i 件物品的体积是Ci，价值是Wi。
# 求解将哪些物品装入背包可使价值总和最大。

# 子问题：另 f(i, V) 为 前i个元素中所能获取的价值最大值，则有：
# f(i, V) = max( f(i-1, V), f(i-1, V-items[i])+values[i] )
#                   ↑                  ↑
#                  放                 不放
# 边界条件：当V小于0或者i<0时，return 0

import functools

cache = {}
def _cache(func):
    def wrapper(i, V):
        if (i, V) in cache: return cache[(i, V)]
        else: 
            cache[(i, V)] = func(i, V)
            return cache[(i, V)]
    return wrapper

def Knapsack01(items, values, V):
    return f(len(items)-1, V)

@_cache
def f(i, V):
    if V < 0 or i < 0: return 0
    return max(f(i-1, V), f(i-1, V-items[i]) + values[i])

def parse_res(cache, i, V):
    res = []
    while i > 0:
        if cache[(i-1, V)] > cache[(i-1, V-items[i])]:
            res.append(0)
        else:
            res.append(1); V = V-items[i]
        i -= 1
    return list(reversed(res))

if __name__ == "__main__":
    items = [2,5,3,4,7,2,4,6]
    values = [4,2,3,5,7,4,6,2]
    V = 15
    res = Knapsack01(items, values, V)
    print(res)