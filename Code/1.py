# 문제1 : 리스트의 삭제

# 리스트는 삭제하는 법
# remove, pop, del 등이 있음. 각각 사용하는 방법이 다름.

# remove : 
# list.remove()로 사용. 리스트레서 첫 번째 항목을 제거. 리스트 요소를 타라미터로 전달.
# 위치 신경쓰지 않고 사용.
# 삭제하려는 항목이 없거나, 인자가 1개 이상 들어갈 때 에러 발생.

# del :
# del object_name으로 사용

# pop()
# list.pop()로 사용.
# list.pop()은 지정된 인덱스에서 요소를 제거하고 반환.
# 파라미터에 인덱스를 지정해 주지 않으면 목록의 마지막 요소가 제거.

nums = [100, 200, 300, 400, 500]
nums.remove(400)
nums.remove(500)
print(nums)

nums = [100, 200, 300, 400, 500]
del nums[3]
del nums[3]
print(nums)

nums = [100, 200, 300, 400, 500]
del nums[nums.index(400)]
del nums[nums.index(500)]
print(nums)

nums = [100, 200, 300, 400, 500]
nums.pop(3)
nums.pop(3)
print(nums)

list1 = []
nums = [100, 200, 300, 400, 500]
for i in nums:
    if i <= 300:
        list1.append(i)
    print(list1)