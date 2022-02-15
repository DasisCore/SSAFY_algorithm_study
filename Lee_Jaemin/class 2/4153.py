while True:
    triangle=list(map(int,input().split()))
    #정렬
    for i in range(3)[::-1]:
        for j in range(i):
            if triangle[j] > triangle[j+1]:
                triangle[j],triangle[j+1] = triangle[j+1],triangle[j]
    
    if triangle == [0,0,0]:
        break
    if triangle[2]**2 == triangle[0]**2+triangle[1]**2:
        print('right')
    else:
        print('wrong')
    