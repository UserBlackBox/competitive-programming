// https://binarysearch.com/problems/Arithmetic-Sequence-Permutation

class Solution {
    solve(nums) {
        nums = nums.sort((a,b)=>a-b);
        let diff = nums[1]-nums[0];
        for(let i=0;i<nums.length-1;i++){
            if(nums[i+1]-nums[i]!==diff) return false;
        }
        return true;
    }
}
