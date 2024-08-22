class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            if maxf < count[s[right]]:
                maxf = count[s[right]]

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
