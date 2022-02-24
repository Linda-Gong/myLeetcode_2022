# similiar 210  Course Schedule II
# Leetcode: 1136. Parallel Courses


# relations: List[List[int]]
class Solution:
    def minimumSemesters(self, n: int, relations) -> int:
        indegree = [0]*(n+1)
        graph = {}
        for relation in relations:
            # a -> b
            a, b = relation[0], relation[1]
            indegree[b] += 1
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)


        #initial queue
        queue = []
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)


        # BFS
        ans = 0
        count = 0
        while queue:
            ans += 1
            next_queue = []
            for node in queue:
                count += 1
                if node in graph:
                    neighbors = graph[node]
                    for ni in neighbors:
                        indegree[ni] -= 1
                        if indegree[ni] == 0:
                            next_queue.append(ni)

            queue = next_queue

        if count == n:
            return ans
        return -1




