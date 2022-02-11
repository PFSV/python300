'''
list = []

for i in range(2,100,2):
    list.append(i)
tlist= tuple(list)
print(tlist)
'''

tuple = tuple(range(2,100,2))
print(tuple)
'''
튜플이 변경이 안 된단거지, 처음 만들 때 설정해두는 건 ok

range는 숫자의 나열을 만들어주는 함수
range(start,end,step)의 구조로 이루어져 있는데,
start부터 end까지 step으로 퐁당퐁당하면서 숫자 나열을 만들어줘
위에건 2부터 100까지 2씩 뛰면서(2,4...) 숫자 나열 만들어줘
'''