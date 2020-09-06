# https://leetcode-cn.com/problems/flood-fill/

class Solution:
    def __init__(self):
        self.visited = set()
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''DFS'''
#         if (sr, sc) in self.visited: return
#         val = image[sr][sc]
#         image[sr][sc] = newColor
#         self.visited.add((sr, sc))
#         # 上
#         if sr-1 >= 0 and image[sr-1][sc] == val:
#             self.floodFill(image, sr-1, sc, newColor)
#         # 下
#         if sr+1 < len(image) and image[sr+1][sc] == val:
#             self.floodFill(image, sr+1, sc, newColor)
#         # 左
#         if sc-1 >= 0 and image[sr][sc-1] == val:
#             self.floodFill(image, sr, sc-1, newColor)
#         # 右
#         if sc+1 < len(image[0]) and image[sr][sc+1] == val:
#             self.floodFill(image, sr, sc+1, newColor)
        
#         return image

        '''bfs'''
        q = deque([(sr, sc)])
        oldColor = image[sr][sc]
        while q:
            x, y = q.popleft()
            image[x][y] = newColor
            if x-1 >= 0 and image[x-1][y] == oldColor and (x-1, y) not in self.visited:
                q.append((x-1, y))
                self.visited.add((x-1, y))
            if x+1 < len(image) and image[x+1][y] == oldColor and (x+1, y) not in self.visited:
                q.append((x+1, y))
                self.visited.add((x+1, y))
            if y-1 >= 0 and image[x][y-1] == oldColor and (x, y-1) not in self.visited:
                q.append((x, y-1))
                self.visited.add((x, y-1))
            if y+1 < len(image[0]) and image[x][y+1] == oldColor and (x, y+1) not in self.visited:
                q.append((x, y+1))
                self.visited.add((x, y+1))
        return image