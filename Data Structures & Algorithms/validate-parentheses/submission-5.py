class Solution:
    def isValid(self, s: str) -> bool:
        # We are gauranteed that the following only has brackets
        bracket_map = {
            "(": ")",
            "{": "}",
            "[":"]"
        }
        brackets = []
        # For loop to put the following brackets into a stack 
        for bracket in s:
            if bracket in bracket_map:
                brackets.append(bracket)
            elif brackets:
                bracket_in_stack = brackets.pop() 
                if bracket != bracket_map.get(bracket_in_stack):
                    return False
            else:
                return False 

        return True if not brackets else False


        
