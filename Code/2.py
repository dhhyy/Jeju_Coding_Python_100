# 문제2 : 리스트의 내장함수

l = [200, 100, 300]
l.insert(2, 10000)
print(l)

# insert :
# list.insert(index, element)
# 리스트 안에 리스트, 딕셔너리, 튜플 등 삽입 가능

mixed_list = [[1,2,3], {7,8,9}]
tuple      = (4,5,6)
mixed_list.insert(1, tuple)
print(mixed_list)