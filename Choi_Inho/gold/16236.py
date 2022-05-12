# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#
#


X, Y = map(int, input().split())
my_max = 0

for h in range(min(X, Y)):
    my_max = max(my_max, (X - 2 * h) * (Y - 2 * h) * h)

print(my_max)