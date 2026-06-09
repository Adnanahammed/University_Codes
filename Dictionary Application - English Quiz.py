words = {'사과':'apple', '컴퓨터':'computer', '학교':'school', '책상':'desk', '의자':'chair'} 

for key in words : 
    
    in_word = input('%s에 해당되는 영어 단어를 입력해주세요: ' % key) 

    if in_word == words[key] : 
        print('정답입니다!') 
    else : 
        print('틀렸습니다!')
