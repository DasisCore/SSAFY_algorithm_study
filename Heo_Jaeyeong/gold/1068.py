# 1068. 트리

# 문제
# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
# 예를 들어, 다음과 같은 트리가 있다고 하자.
# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.
# 이제 리프 노드의 개수는 1개이다.
#
# 입력
# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.
#
# 출력
# 첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

###########################################################################################

def order(v):
    global cnt
    
    # 노드를 타고 밑으로 내려감
    if tree[v]:
        for i in tree[v]:
            order(i)

    # 더이상 연결된 노드가 없다면 cnt +1
    else:
        cnt += 1


n = int(input())
li = list(map(int, input().split()))
tree = [[] for i in range(n)]
# 제거할 노드
d = int(input())


a = [] # 루트 노드를 넣을 리스트
for i in range(n):
    # 루트 노드 넣기
    if li[i] == -1:
        a.append(i)
    # 트리 만들기 + 제거할 노드라면 넣지 않는다.
    # 부모 노드와 자식노드의 연결을 끊음.
    if li[i] != -1 and i != d:
        tree[li[i]].append(i)

cnt = 0
# 각 루트 노드를 기준으로 order를 실행
for i in a:
    if i != d:
        order(i)
print(cnt)
