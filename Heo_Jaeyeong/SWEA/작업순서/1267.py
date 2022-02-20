# 1267. 작업순서

v, e = map(int, input().split())
li = list(map(int, input().split()))

arr = []
while len(li) > 0:
    temp = li[:2]
    arr.append(temp)
    li = li[2:]

# 예제 기준
# li
# [[4, 1], [1, 2], [2, 3], [2, 7], [5, 6], [7, 6], [1, 5], [8, 5], [8, 9]]

graph = {}
for i in arr:
    if not i[0] in graph:
        graph[i[0]] = [i[1]]
    else:
        graph[i[0]].append(i[1])
# graph
# {4: [1], 1: [2, 5], 2: [3, 7], 5: [6], 7: [6], 8: [5, 9]}

# 여기까지밖에 모르겠습니당... BFS 사용해야하는건 알겠는데..

