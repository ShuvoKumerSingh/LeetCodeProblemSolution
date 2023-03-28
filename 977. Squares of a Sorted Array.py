class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_lst=[]
        i=0
        lenth=len(nums)
        while lenth>0:
            new_lst.append(nums[i]*nums[i])
            i+=1
            lenth-=1
        return sorted(new_lst,reverse=False)
    
    
    '''
    Another Solution using Two pointer
    '''
    class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_lst=[]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]**2<=nums[r]**2:
                new_lst.append(nums[r]**2)
                r-=1
            else:
                new_lst.append(nums[l]**2)
                l+=1
        return new_lst[::-1]
