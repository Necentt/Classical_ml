nums = [0,2,3,4,6,8,9]


start = nums[0]
result = []
for i in range(len(nums) - 1):
    if (nums[i] + 1 == nums[i + 1]) and (i == len(nums) - 2):
        result.append(f"{start}->{nums[-1]}")
        break
    elif nums[i] + 1 == nums[i + 1]:
        continue
    elif start == nums[i]:
        result.append(str(start))
        start = nums[i + 1]
    else:
        result.append(f'{start}->{nums[i]}')
        start = nums[i + 1]
        print(nums[i],start)

if start == nums[-1]:
    result.append(str(start))
print(result)
