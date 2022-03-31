def bfs(p):
    q = [p]
    visited = [1] + [0]*N
    cnt = 0
    while 0 in visited:
        x = q.pop(0)
        for r in rs[x]:
            if not visited[r]:
                visited[r] = 1
                q.append(r)
        cnt += 1
    return cnt


N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]
rs = [set() for _ in range(N+1)]
my_min = 500000
for relation in friends:
    rs[relation[0]].add(relation[1])
    rs[relation[1]].add(relation[0])
for num in range(1, N+1):
    my_min = min(my_min, bfs(num))
print(my_min)