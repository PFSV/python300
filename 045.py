file_name = "보고서.xlsx"

print(file_name.endswith(("xlsx","xls")))

'''
.endswith() 이 문자열이 이걸로 끝나는지 검사해주는 함수

string.endswith(value,start,end)

보통, start와 end가 없을 시, 모든 문자열을 검사한다.

> 이 string이 value의 값으로 끝나는지 검사할건데, 
start부터 end 바로 앞까지 검사한다.
검사 결과는 bool type으로 제공합니다.

* 위 예제의 경우, 검사해야할 value가 두 개이기 때문에, ()로 묶어서, value 영역을 채워준다.

hz = "Homzzang.com"

x = hz.endswith("zz",1,5)

hz에 해당하는(Homzzang.com) 문자열의 두 번째 글자부터 
4번째 글자(인덱스1부터5까지)까지 검사를 해서, 이게 "zz"로 끝나는지 확인한다
'''