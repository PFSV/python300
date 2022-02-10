data = "   삼성전자    "

stripped_data= data.strip()

print(stripped_data)


data2 = "000한국외대000"
strip2 = data2.strip("0")
print(strip2)

'''
문자열.strip()쓰면 좌우 ()내부의 내용이 없어진다.
빈칸이면 공백이 사라집니다.

lstrip("지울애")이면 지울 애 왼쪽 꺼
rstrip("지울애")이면 지울 애 오른쪽 꺼
'''
