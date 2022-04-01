def bfs(p):
    global my_min, people
    q = [p, 0]
    visited = [1] + [0]*N
    cnt = 0
    while 1:
        x = q.pop(0)
        if x == 0:
            cnt += 1
            q.append(0)
            if not 0 in visited:
                break
        else:
            for r in rs[x]:
                if not visited[r]:
                    visited[r] = 1
                    q.append(r)
    if cnt < my_min:
        people = p
        my_min = cnt


N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]
rs = [set() for _ in range(N+1)]
my_min = 500000
people = 1
for relation in friends:
    rs[relation[0]].add(relation[1])
    rs[relation[1]].add(relation[0])
for num in range(1, N+1):
    bfs(num)
print(people)