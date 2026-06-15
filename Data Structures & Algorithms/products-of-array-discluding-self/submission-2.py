class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # For 3: 1 * 2 (prefix) * (suffix) 4 * 5 
        # [1, 2, 3, 4, 5]
        # 1 1 2 6 24 # Prefix
        # 120 60 20 5 1 # Suffix
        # result = 120 60 40 30 24

        len_nums = len(nums)
        result_list = [1] * len_nums
        value = 1
        # Doing prefix pass
        for i in range(len_nums):
            # if (i == 0):
            #     continue
            result_list[i] = (value) # Doing this first avoids the need for the conditional
            value *= nums[i]
        
        # Doing the suffix pass
        value = 1
        for i in range(len_nums - 1, -1, -1):
            # if (i == len_nums - 1 ):
            #     continue
            result_list[i] *= value
            value *= nums[i]
        
        return result_list
