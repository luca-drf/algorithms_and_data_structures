def dfs_route(V, E, start, dest):
    stack = [start]
    V.remove(start)
    while stack:
        print stack
        visiting = stack.pop()
        print 'Visiting:', visiting
        if visiting == dest:
            return True
        for edge in E:
            if edge[0] == visiting and edge[1] in V:
                stack.append(edge[1])
                V.remove(edge[1])
    return False


def bfs_route(V, E, start, dest):
    queue = [start]
    V.remove(start)
    while queue:
        print queue
        visiting = queue.pop()
        print 'Visiting:', visiting
        if visiting == dest:
            return True
        for edge in E:
            if edge[0] == visiting and edge[1] in V:
                queue.insert(0, edge[1])
                V.remove(edge[1])
    return False


if __name__ == '__main__':
    V = ['u', 'v', 'w', 'x', 'y', 'z']
    E = [('u', 'x'), ('u', 'v'), ('v', 'y'), ('w', 'y'), ('w', 'z'),
         ('x', 'v'), ('y', 'x'), ('z', 'z')]

    print '= DFS ='
    print dfs_route(V, E, 'u', 'z')
    print ''

    V = ['u', 'v', 'w', 'x', 'y', 'z']
    E = [('u', 'x'), ('u', 'v'), ('v', 'y'), ('w', 'y'), ('w', 'z'),
         ('x', 'v'), ('y', 'x'), ('z', 'z')]
    print '= BFS ='
    print bfs_route(V, E, 'u', 'z')
