T = input()
alphals=[]
alphals.extend('abcdefghijklmnopqrstuvwxyz')
solve = [-1]*26

cnt=0
for i in T:
    if solve[alphals.index(i)] == -1:
        solve[alphals.index(i)]=cnt
        cnt +=1
    else:
        cnt +=1
print(*solve)
