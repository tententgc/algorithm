nums = [2, 7, 11, 15]
target = 9
def twosum(nums, target) :
    dic = dict()

    for val, key in enumerate(nums):
        if key not in dic:
            dic[key] = [val]
        else:
            dic[key].append(val)

    for key, val in dic.items():
        if target - key in dic:
            if key != target - key:
                return [dic[key][0], dic[target - key][0]]
            elif len(dic[key])  > 1:
                return [dic[key][0], dic[key][1]]

print(twosum(nums, target)) 