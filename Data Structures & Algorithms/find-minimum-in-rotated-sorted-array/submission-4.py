class Solution:
    def findMin(self, nums: List[int]) -> int:

       # Information:
       # - There is only two halves of the sequence divided by the pivot
       # - All values from pivot point to leftmost value are sorted in ascending order
       # Leftmost value will determine if a value is part of the ascending sequence (
       # left half) if the value is bigger than it
       # If value is less than the leftmost than the value is not part of the same sequence
       # and is on the lesser sequence

       # If the sequence is not apart of the leftmost sequence than it is < leftmost  
       # If the sequence is apart of the leftmost sequence than it is >= leftmost because
       # leftmost is the smallest in the sequence 

       # If apart of the sequence than search to the right (where smaller values could exist)

       # If not apart of the sequence than search to then search to the left 
       # (where the smaller values of the sequence is)

       l, r = 0, len(nums) - 1 
       min_val = nums[0]
       while (l <= r): # Needed the equal because of the case when only one value
        # Optimization if we know that the whole sequnce is already sorted
        if (nums[l] < nums[r]):
            min_val = min(min_val, nums[l])
            break

        mid = (l + r) // 2
        min_val = min(nums[mid], min_val)

        # Part of the sequence (smallest value is leftmost)
        if nums[mid] >= nums[l]:
            # Search the right half in case of smaller numbers
            l = mid + 1
        # Not part of the sequence
        elif nums[mid] < nums[l]:
            # Search the left half of current sequence (everything to the right of 
            # smaller this sequnce half is larger)
            r = mid - 1

       return min_val