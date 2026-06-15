class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # Need to skip values that are the same 
       # Target is 0
       # Start with a sorted array so that it gives us the following information
       # - Values that are on the left are smaller than the right
       # - Can avoid duplicate values

       # in place sorting
       nums.sort();  # EX: [-4, -1, -1, 0, 1, 2] 
       result = []
       for i, num in enumerate(nums):
        # This is needed to skip dups of third leftmost value
        if (i > 0 and num == nums[i-1]):
            continue
        # Two sum solution (both left and right can also have dups,
        # but taking care of the left pointer dup changes one of the
        # values, making right fine with dups)
        l, r = i + 1, len(nums) - 1 
        while (l < r):
            indicator = num + nums[l] + nums[r]
            
            if indicator > 0:
                r-=1
            elif indicator < 0:
                l+=1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1 
                while l < r and nums[l] == nums[l-1]:
                    l+=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
                
       return result
                    


