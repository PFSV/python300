phone_number = "010-1111-2222"
new_phone_number = phone_number.replace("-"," ")
print(new_phone_number)

'''
replace method는 문자열의 일부 부분을 바꿔줌
문자열.replace("기존","신규")
>'기존' 문자열이 '신규' 문자열로 바뀐다!

단, 문자열은 수정이 불가능하므로 replace를 한 문자열을
 새로운 문자열로 바인드해줘야한다.

'''