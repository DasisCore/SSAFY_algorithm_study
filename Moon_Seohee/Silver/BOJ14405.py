# BOJ14405 피카츄

S = input()
ans = "YES"
tem = 0
while tem < len(S):
    if S[tem] == "p":
        tem += 1
        if tem >= len(S) or S[tem] != "i":
            ans = "NO"
            break
    elif S[tem] == "k":
        tem += 1
        if tem >= len(S) or S[tem] != "a":
            ans = "NO"
            break
    elif S[tem] == "c":
        tem += 1
        if tem >= len(S) or S[tem] != "h":
            ans = "NO"
            break
        elif tem >= len(S) or S[tem] == "h":
            tem += 1
            if tem >= len(S) or S[tem] != "u":
                ans = "NO"
                break
    else:
        ans = "NO"
        break
    tem += 1
print(ans)