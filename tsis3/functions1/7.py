def has_33(nums):
    for i in range(len(nums)):
        if i == len(nums)-1: continue
        if nums[i] == nums[i+1] == 3 : return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))