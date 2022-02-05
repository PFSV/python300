#print("first");print("second")

print("first",end="");print("second")


#예시
print("first");print("second")


'''
한 줄에 여러 코드를 짜고 싶으면 ;로 이어주기

print는 출력한 값 뒤에 기본값으로 \n을 붙여줌
근데 여기에 ,end="완료문자"를 넣으면 "완료문자"로 커스텀 가능함
>출력 완료문자를 "완료문자"로 하겠다.

기본적으로 출력이 어떻게 되는지 보자
예시 출력시
first
second
로 나옴.
> 기본적으로 print 뒤에 \n이 붙어있음

근데 이걸 end=""로 바꿔주면, 
완료문자를 지워준거랑 마찬가지니까 두 출력값이 붙어 나옴
'''