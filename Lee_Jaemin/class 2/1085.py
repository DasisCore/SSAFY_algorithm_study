x,y,w,h = map(int,input().split())
a=w-x
b=h-y
solve = [x,y,a,b]
mmin=x
for i in solve:
    if mmin > i:
        mmin = i
print(mmin)