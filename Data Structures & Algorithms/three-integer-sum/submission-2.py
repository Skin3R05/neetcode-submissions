class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            # in this statement I am skipping duplicate elements in a list
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # initialize pointers 
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                # regulate pointers movement    
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])


                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 
 
                    l += 1
                    r -= 1
        return res
                
