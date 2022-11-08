import collections
def solve(strs):
    dic=collections.defaultdict(list)
    for strr in strs: 
        dic["".join(sorted(strr))].append(strr)
    res = []
    for k,val in dic.items():
        res.append(val)
            
    return res

print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))