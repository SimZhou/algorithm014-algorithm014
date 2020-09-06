# https://leetcode-cn.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q, indegree, outdegree = collections.deque(), collections.defaultdict(int), collections.defaultdict(list)
        # 准备工作
        studied = 0
        for i in range(numCourses):
            indegree[i], outdegree[i]
        for c, pre in prerequisites:
            indegree[c] += 1
            outdegree[pre].append(c)
        # 拓扑排序
        for c in indegree: 
            if indegree[c] == 0: q.append(c)
        while q:
            study, studied = q.popleft(), studied + 1
            for nextcourse in outdegree[study]:
                indegree[nextcourse] -= 1
                if indegree[nextcourse] == 0: 
                    q.append(nextcourse)
        
        return studied == numCourses