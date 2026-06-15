class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # Need to skip values that are the same 
       # Target is 0
       # Start with a sorted array so that it gives us the following information
       # - Values that are on the left are smaller than the right
       # - Can avoid duplicate values

       nums.sort()
       result = []
       
       # Fix one of the values i
       for i, num in enumerate(nums):
        # Skip the current num value
        if (i > 0 and num == nums[i-1]):
           continue 

        # Regular two sum problem
        l, r = i+1, len(nums) - 1 
        while (l < r):
            val = num + nums[l] + nums[r]
            if (val < 0):
                l+=1 
            elif (val > 0):
                r-=1
            else:
                result.append([num, nums[l], nums[r]])
                l+=1
                # Need to make sure that we skip duplicate l values,
                # updating the l value will make it unique so it doesn't
                # matter if r value has duplicates
                while ( l < r and nums[l] == nums[l-1]):
                    l+=1
       return result

