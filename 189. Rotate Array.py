class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
'''
Another Solution 
"'
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenth=len(nums)
        l,r=0,lenth-1
        
        if lenth==k:
            return nums
        elif lenth<k:
             while k-lenth>0:
                if nums[l]<nums[r]:
                    nums.insert(0,nums[r])
                    nums.pop(r+1)
                    r=r
                    l=l+1
                k-=1
        else:
            while k>0:
                if nums[l]<nums[r]:
                    nums.insert(0,nums[r])
                    nums.pop(r+1)
                    r=r
                    l=l+1
                    k-=1
                else:
                    nums.insert(0,nums[r])
                    nums.pop(r+1)
                    r=r
                    l=l+1
                    k-=1
