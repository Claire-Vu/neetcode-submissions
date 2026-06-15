class Solution:
    def findMin(self, nums: List[int]) -> int:
       # We can start from the middle and know more information  
       # But the array is rotated between 1 and n times

       # Even with rotation all the values to the left is smaller
       # and we are only trying to find the min

       # Ex: [6, 1, 2, 3, 4, 5]
       # Start at the middle // and set that as min
       # Left half check mid
       # if mid is more than current continue 
       # Need to use recursion

       mid = len(nums) // 2
       l, r = 0, len(nums) - 1 
       
       if (len(nums) == 1):
        return nums[0]
       # Getting the min of left half
       min_left = self.findMin(nums[l:mid])
       # Getting the min of right half
       min_right = self.findMin(nums[mid:r+1])
       return min(min_left, min_right)


    
