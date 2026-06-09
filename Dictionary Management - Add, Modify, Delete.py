name = '아드난' 
scores = {'kor': 95, 'eng': 85, 'math': 90, 'science': 80} 
print(scores) 

scores['kor'] = 70  
print(scores['kor']) 
scores['music'] = 100    
print(scores) 
del scores['science']
print(scores) 
print('이름 : %s' % name) 
print('국어 : %d' % scores['kor']) 
print('영어 : %d' % scores['eng']) 
print('수학 : %d' % scores['math'])
