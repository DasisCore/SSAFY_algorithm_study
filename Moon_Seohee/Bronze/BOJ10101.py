# BOJ10101 삼각형 외우기
A = int(input())
B = int(input())
C = int(input())

if A == 60 and A == B and B == C:
    print("Equilateral")
elif A + B + C == 180:
    if A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")