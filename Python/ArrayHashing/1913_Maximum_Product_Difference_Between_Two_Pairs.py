class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        max_1, max_2 = 0, 0
        min_1, min_2 = float("inf"), float("inf")
        for num in nums:
            if num > max_1:
                max_1, max_2 = num, max_1
            elif num > max_2:
                max_2 = num
            if num < min_1:
                min_1, min_2 = num, min_1
            elif num < min_2:
                min_2 = num
        return max_1 * max_2 - min_1 * min_2
