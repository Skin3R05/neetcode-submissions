class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        filtered_nums = sorted(set(nums))
        if not nums:
            return 0
        
        current_streak = 1
        longest_streak = 1
        for i in range(len(filtered_nums) - 1):
            if filtered_nums[i+1] == filtered_nums[i] + 1:
                current_streak +=1
            else: 
                longest_streak = max(current_streak, longest_streak)    
                current_streak = 1
        return max(longest_streak, current_streak)