#BOJ2495 연속 구간
for tc in range(3):
    s = str(input())
    cntmax = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt+=1
        else:
            cntmax=max(cnt,cntmax)
            cnt=1
    cntmax = max(cnt, cntmax)
    print(cntmax)