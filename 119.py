fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

if input("수진이가 좋아하는 계절이 뭐게?") in fruit.keys():
    print("정답이야.")
else:
    print("오답이야.")

'''
in 뒷부분엔 iterable한 자료가 들어갑니다.
'''