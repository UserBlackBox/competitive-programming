# https://binarysearch.com/problems/Packing-Boxes

class Solution:
    def solve(self, nums):
        lst = []
        for i in range(len(nums)):
            if i == 0:
                lst.append([nums[0]])
                continue
            if nums[i] == nums[i-1]:
                lst[-1].append(nums[i])
            else:
                lst.append([nums[i]])
        return lst

