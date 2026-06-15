class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left and right pointers both start at the same 0 index
        # initialize a set and add the current value into the set
        # right move one
        
        # If the char of right not in set, add it and count+= 1

        # If the char is in set, move left to location
        # without the duplicate char and subtract that from the count however many
        # we moved left

        # right +=1 

        # "zxyzxayz"

        l, r = 0, 0
        max_count = 0
        curr_count = 0
        chars_in_seq = set()
        while (r < len(s)):
            if (s[r] not in chars_in_seq):
                chars_in_seq.add(s[r]);
                curr_count+=1
                r += 1
            else:
                max_count = max(curr_count, max_count)
                # We need to see what letter it was that was duplicate and shift left there
                while (l < r and s[l] != s[r]):
                    chars_in_seq.remove(s[l])
                    l+=1
                    curr_count-=1
                chars_in_seq.remove(s[l])
                l+=1
                curr_count-=1
        return max(curr_count, max_count)


        