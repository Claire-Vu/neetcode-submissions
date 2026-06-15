class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter all non alphanumeric charaters
        # filtered_string=""
        # for letter in s:
        #     if letter.isalnum():
        #         filtered_string+=letter.lower()
        # return filtered_string == filtered_string[::-1]

        # Using space complexity O(1) method
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
            
        
    
    def isalphanum(self, letter: chr) -> bool:
        # Alternative
        # alpha = "abcdefghijklmnopqrstuvwxyz"
        # nums = "0123456789"
        _letter = letter.lower()
        return  ('a') <= ord_letter <= ('z') or \
       ('0') <= ord_letter <= ('9')
        