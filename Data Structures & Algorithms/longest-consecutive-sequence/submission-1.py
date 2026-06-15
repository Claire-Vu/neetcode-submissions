class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums);
        print(unique_nums)
        max_con = 0
        for num in unique_nums:
            if (num - 1) not in unique_nums:
                count=1
                curr_num=num
                while (curr_num + 1) in unique_nums:
                    count+= 1
                    curr_num+=1
                if (count > max_con):
                    max_con = count
        return max_con;
                