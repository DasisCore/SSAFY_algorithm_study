# 백준 1085번 직사각형에서 탈출
x, y, w, h = map(int,input().split())
result = x
if y < x:
    result = y
if y - h >= 0 and y - h < result:
    result = y - h
if h - y >= 0 and h - y < result:
    result = h - y
if x - w >= 0 and x - w < result:
    result = x - w
if w - x >= 0 and w - x < result:
    result = w - x

print(result)