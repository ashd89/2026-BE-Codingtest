class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            substring = set()
            j = i
            while j < len(s):
                c = s[j]
                if c in substring:
                    break
                # print(c, end='')
                substring.add(c)
                j += 1
            # print('')
            result = max(j - i, result)
        return result
        
