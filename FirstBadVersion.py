class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = n
        while left<=right:
            mid = left + (right-left)//2
            if isBadVersion(mid):
                result = mid
                right = mid-1
            else:
                left = mid+1
        return result