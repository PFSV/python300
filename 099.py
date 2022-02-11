
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

print(dict(zip(keys,vals)))

'''
zip function은 튜플을 합쳐주는데 사용
튜플 내 순서에 맞는 것끼리 합쳐져서 새로운 튜플들을 반환하나, zip 형태로.
(1,2,3),(a,b,c)라면 (1,a),(2,b).(3,c)의 구조로 합침
넘치는 건 자름

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

a와 b 튜플의 요소들을 순서대로 짝지어서 새롭게 연결하되, zip 형태로 산출하세요
>나중에 원하는 모양으로 가공하세요
'''