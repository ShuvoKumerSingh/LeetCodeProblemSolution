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