# BOJ2920 음계
music = list(map(int, input().split()))
scale = ["c", "d", "e", "f", "g", "a", "b", "C","x"]
result =""
for i in range(8):
    a = scale[music[i]-1]
    result += (a)
if result == "cdefgabC":
    print("ascending")
elif result == "Cbagfedc":
    print("descending")
else:
    print("mixed")