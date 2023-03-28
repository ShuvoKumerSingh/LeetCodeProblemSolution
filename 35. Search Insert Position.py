class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        mid=l+(r-l)//2
        while l<=r:
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
            mid=l+(r-l)//2
        if nums[mid]==target:
            return mid
        else:
            index=0
            i=0
            lenth=len(nums)
            while lenth>0:
                if nums[i]<target:
                    index=i+1
                i+=1
                lenth-=1
            return index
