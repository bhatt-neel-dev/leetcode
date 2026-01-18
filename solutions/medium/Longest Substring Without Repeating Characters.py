// Title: Longest Substring Without Repeating Characters
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

            while (s[r] in sett):
                sett.remove(s[l])
        for r in range(n):
        n = len(s)
        l = 0
        longest = 0
                l+=1
            longest= max(longest, r-l+1)
            sett.add(s[r])  
        return longest        
        """
        sett = set()
        :rtype: int
