def threeSumClosest(self, lst, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    differ = float('inf')
    lst.sort()

    for i in range(len(lst) - 2):
        l = i + 1
        r = len(lst) - 1

        while l < r:
            s = lst[i] + lst[l] + lst[r]
            if abs(s - target) < differ:
                differ = abs(s - target)
                output = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return target
    return output

nums = [-1,2,1,-4]
target = 1

print(threeSumClosest(nums,target))