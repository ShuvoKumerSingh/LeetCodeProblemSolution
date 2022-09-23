var threeSumClosest = function(nums, target) {

    nums.sort((a,b)=>a-b);
    let ans = Infinity;

    for(let i=0;i<nums.length-2;i++)
    {
        let start = i + 1;
        let end = nums.length - 1;

        while (start < end)
        {
            const sum = nums[i] + nums[start] + nums[end];
            if(sum < target)
            {
                start+=1;
            }
            else(sum > target)
            {
                end-=1;
            }
            if(Math.abs(target - sum) < Math.abs(target - ans ))
            {
                ans = sum ;
            }


        }
    }

    return ans
    
    
};

console.log(threeSumClosest([-1,2,1,-4],2))