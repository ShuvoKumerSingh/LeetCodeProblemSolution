var runningSum = function(nums) {
    const reslt_lst = [];
    reslt_lst[0] = nums[0];
    for(let i=1;i<nums.length;i++)
    {
        reslt_lst[i] = nums[i] + reslt_lst[i-1];
    }
    return reslt_lst;
    
    
};

let num = [1,2,3,5];
console.log(runningSum(num));