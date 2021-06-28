// https://binarysearch.com/problems/Largest-Gap

class Solution {
    solve(nums) {
        nums = nums.sort((a, b) => a - b);
        let largest = 0;
        for(let i=0;i<nums.length-1;i++){
            if(nums[i+1]-nums[i]>largest) largest = nums[i+1]-nums[i];
        }
        return largest;
    }
}
