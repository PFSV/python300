a,b, *c = (0,1,2,3,4,5)
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a,b = scores

print(valid_score) 


'''
star expression; 언패킹 시 여러번 써야 할 거 압출해놓음
'''