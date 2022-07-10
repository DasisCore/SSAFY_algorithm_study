# BOJ1264
mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", "U"]
while True:
    moon = input()
    if moon == "#":
        break
    else:
        cnt = 0
        for i in moon:
            if i in mo:
                cnt += 1
    print(cnt)