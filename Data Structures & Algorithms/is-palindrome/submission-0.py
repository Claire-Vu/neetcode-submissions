class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter all non alphanumeric charaters
        filtered_string=""
        for letter in s:
            if (self.isalphanum(letter)):
                filtered_string+=letter.lower()
        return filtered_string == filtered_string[::-1]
    
    def isalphanum(self, letter: chr) -> bool:
        # alpha = "abcdefghijklmnopqrstuvwxyz"
        # nums = "0123456789"
        # print(letter)
        ord_letter = ord(letter.lower())
        return  ord_letter >= ord('a') and ord_letter < ord('z') or \
        ord_letter >= ord('0') and ord_letter <= ord('9')
        