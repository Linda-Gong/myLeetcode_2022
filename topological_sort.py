#210 Course Schedule II
# similiar 1136
# topolpgical sort
def findOrder(numCourses, prerequisities):
    indegree = [0] * numCourses
    graph = {}
    # a, b
    # b -> a
    ## construct the graph and indegree
    for relation in prerequisities:
        a, b = relation[0], relation[1]
        indegree[a] += 1
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    #### BFS - initial
    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    # BFS
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node)
        if node in graph:
            node_list = graph[node]
            for n in node_list:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

    # check if there's a circle in graph
    if len(res) == numCourses:
        return res

    return []




print(findOrder(2, []))
