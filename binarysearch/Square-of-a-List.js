// https://binarysearch.com/problems/Square-of-a-List

class Solution {
    solve(nums) {
        for(let i=0;i<nums.length;i++) nums[i] *= nums[i];
        nums = nums.sort((a,b) => a-b);
        return nums;
    }
}
