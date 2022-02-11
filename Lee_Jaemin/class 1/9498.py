T = int(input())
grade=['A','B','C','D','F']
T -= 60

if T >= 30:
    print(grade[0])
elif T >= 20:
    print(grade[1])
elif T >= 10:
    print(grade[2])
elif T >= 0:
    print(grade[3])
else:
    print(grade[4])