a = "hello world"
a = a.split(" ")
print(a)

test = 'Hello world 헬로 월드'
print(test.split(" ",maxsplit=2))

'''
문자열.split("구분자",maxsplit=n) 
문자열을 split 내 구분자 기준으로 나눠서, 나눈 걸 list 안에 넣겠습니다.
구분자는 아무것도 안 넣으면 기본값이 공백이에요.
maxsplit이라는걸로 몇 번 나눌건지 셀 수 있어요-> n번 나눕니다.
두 번째 예시를 보면, 헬로 월드가 하나의 요소로 존재하는데, 그 이유는 ,
두 번 밖에 안 나눴기 때문입니다.


'''