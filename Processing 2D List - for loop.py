scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69], [90, 76, 91], [82, 66, 88], [83, 86, 79], [85, 90, 83]] 

for  i in range(len(scores)) : 
    sum = 0 
    for j in range(len(scores[i])) : 
        sum = sum + scores[i][j] 

    avg = sum/len(scores[i]) 

    print('%d번째 학생의 합계 : %d, 평균 : %.2f' % (i+1, sum, avg))
