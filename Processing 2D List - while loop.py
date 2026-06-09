scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69],  [90, 76, 91], [82, 66, 88], [83, 86, 79], [85, 90, 83]] 

i = 0 
while  i < len(scores) : 
    sum = 0 
    j = 0  
    while j < len(scores[i]) : 
        sum = sum + scores[i][j] 
        j += 1 
                 
    avg = sum/len(scores[i]) 
    print('%d번째 학생의 합계 : %d, 평균 : %.2f' % (i+1, sum, avg)) 
    i += 1
