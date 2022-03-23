# 14453. Hoof, Paper, Scissors (Silver)

# 문제
# You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".
# The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.
# Farmer John wants to play against his prize cow, Bessie, at N games of "Hoof, Paper, Scissors" (1 ≤ N ≤ 100,000). Bessie, being an expert at the game, can predict each of FJ's gestures before he makes it. Unfortunately, Bessie, being a cow, is also very lazy. As a result, she tends to play the same gesture multiple times in a row. In fact, she is only willing to switch gestures at most once over the entire set of games. For example, she might play "hoof" for the first x games, then switch to "paper" for the remaining N−x games.
# Given the sequence of gestures FJ will be playing, please determine the maximum number of games that Bessie can win.
#
# 입력
# The first line of the input file contains N.
# The remaining N lines contains FJ's gestures, each either H, P, or S.
#
# 출력
# Print the maximum number of games Bessie can win, given that she can only change gestures at most once.

####################################################################################


n = int(input())
h = [0]
p = [0]
s = [0]
for i in range(n):
    a = input()
    if a == "H":
        h.append(1)
        p.append(0)
        s.append(0)
    elif a == "P":
        h.append(0)
        p.append(1)
        s.append(0)
    elif a == "S":
        h.append(0)
        p.append(0)
        s.append(1)

prefix1 = [0] * (n + 1)
prefix2 = [0] * (n + 1)
prefix3 = [0] * (n + 1)

answer = 0
for i in range(1, n + 1):
    prefix1[i] = prefix1[i - 1] + h[i]
    prefix2[i] = prefix2[i - 1] + p[i]
    prefix3[i] = prefix3[i - 1] + s[i]

for i in range(1, n + 1):
    answer1 = max(prefix1[i], prefix2[i], prefix3[i])
    answer2 = max(prefix1[n] - prefix1[i], prefix2[n] - prefix2[i], prefix3[n] - prefix3[i] )
    answer = max(answer1 + answer2, answer)
print(answer)
