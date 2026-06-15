class Solution:

    def encode(self, strs: List[str]) -> str:
        # The method is to place in the front of the word
        # a unique character, the first instance of it will
        # tell us where the line break is, even if the letter 
        # appears somewhere else that doesn't matter because we are adding it to
        # the first instance
        results=""
        for word in strs:
            results+= str(len(word)) + "#" + word
        return results

    def decode(self, s: str) -> List[str]:
        # Need i to keep track of where the number start (number could be 100)
        i = 0
        result_list=[]
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1;
            # Now the current letter is #
            len_of_word = int(s[i:j]);
            print(len_of_word)
            print(s[j+1 : j+1+len_of_word])
            result_list.append(s[j+1 : j+1+len_of_word])
            i = j + 1 + len_of_word;
        return result_list
