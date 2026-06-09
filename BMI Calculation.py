''' 
입력: 키, 몸무게 
처리: 체질량지수(BMI)=몸무게(kg)/(키(m))**2 
      18.5 미만 - 저체중, 건강위험도 높음 
      18.5이상 25미만 - 정상체중, 건강위험도 낮음 
      25이상 30미만 - 과체중, 건강위험도 낮음 
      30이상 - 비만, 건강위험도 높음 
출력: BMI, 건강상태 
''' 

height=int(input('키 입력(cm) : ')) 
weight=int(input('몸무게 입력(kg) : ')) 
bmi=weight/(height/100)**2 
print("체질량지수 %.1f :" %bmi, end='') 

if bmi<25: 
    if bmi<18.5: 
        print("저체중, 건강위험도 높음 ") 
    else: 
 
       print("정상체중, 건강위험도 낮음 ") 
else: 
    if bmi<30: 
        print("과체중, 건강위험도 낮음 ") 
    else: 
        print("비만, 건강위험도 높음 ")
