class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_h = 0                                                                       
        max_l = 0                                                                    
        res = 0                                                                                    
        for h in range(len(heights)):                           # n+1               
            for l in range(h, len(heights)):                    # n(n+1)            
                max_l = l - h                                   # n*n               
                max_h = min(heights[l], heights[h])             # n*n               
                res = max(res, max_l * max_h)                   # n*n               
        return res                                              # 1                

        # max_h --> 1
        # max_l --> 1
        # res --> 1
        # h --> 1
        # l --> 1

        # f(n) = 4n^2+2n+2 --> O(n^2)
        # s(n) = O(1)