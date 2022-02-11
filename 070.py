data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)


'''
sort는 정렬한단건데 sort와 sorted 방법이 있다.
둘의 차이는 sort는 정렬하는 대상이 수정되고, sorted는 그렇지 않다는 것
그렇기에 sort는 
iterable.sort()로 바로 쓸 수 있고
sorted는 newiterable = sorted(iterable)로 새로 정렬한 대상을 만들어줘야함
(그래야 원래 데이터가 보존되니까)

sort시리즈는 기본적으로 숫자 오름차순, 알파벳 순서로 진행되며, 기본적으로
iterable.sort(reverse=True|False,key=key)의 구문을 가지고 있다.

reverse를 쓰면 거꾸로 정렬할지 말 지의 문제며 key는 정렬을 목적으로 하는 키를 넣을 수 있다.
가령 sort(reverse=True,key=len)이면 글자 길이가 큰 것부터 정렬시킨다는 뜻
'''