class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # For 3: 1 * 2 (prefix) * (suffix) 4 * 5 
        # [1, 2, 3, 4, 5]
        # 1 1 2 6 24 # Prefix
        # 120 60 20 5 1 # Suffix
        # result = 120 60 40 30 24

        len_nums = len(nums)
        prefix_list = [1] * len_nums
        suffix_list = [1] * len_nums

        # Creating prefix_list
        for i in range(len_nums):
            if (i == 0):
                continue
            else:
                prefix_list[i] = (nums[i - 1] * prefix_list[i - 1])
        
        # Creating the suffix_list
        for i in range(len_nums - 1, -1, -1):
            if (i == len_nums - 1 ):
                continue
            else: 
                suffix_list[i] = (nums[i+1] * suffix_list[i + 1])
        print(f"prefix_list {prefix_list}")
        print(f"suffix_list {suffix_list}")
        
        return [x * y for x, y in zip(prefix_list, suffix_list)]

