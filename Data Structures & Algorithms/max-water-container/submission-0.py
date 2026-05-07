class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_h = 0
        max_l = 0
        res = 0
        for h in range(len(heights)):
            for l in range(h, len(heights)):
                max_l = l - h
                max_h = min(heights[l], heights[h])
                res = max(res, max_l * max_h)
        return res