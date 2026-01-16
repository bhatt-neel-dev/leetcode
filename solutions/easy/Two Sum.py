// Title: Two Sum
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/two-sum/

        """
        for i in range(len(nums)):
        index_map = {}
            if complement in index_map:
                return index_map[complement], i
            complement = target-nums[i]
            index_map[nums[i]] = i
        :rtype: List[int]
        :type target: int
        :type nums: List[int]
        """
class Solution(object):
    def twoSum(self, nums, target):
