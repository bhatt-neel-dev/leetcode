// Title: Two Sum
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/two-sum/

        """
        idx={}
        for i in range(n):
            complement = target - nums[i]
            if complement in idx:
        n=len(nums)
                return idx[complement], i
            idx[nums[i]] = i

