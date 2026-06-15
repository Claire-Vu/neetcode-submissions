class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "(": ")",
            "{": "}",
            "[":"]"
        }
        bracket_close = ")}]"
        brackets = []
        # For loop to put the following brackets into a stack 
        for bracket in s:
            if bracket_map.get(bracket):
                brackets.append(bracket)
            elif bracket in bracket_close:
                if len(brackets) <= 0:
                    return False;
                bracket_in_stack = brackets.pop()
                if bracket_map[bracket_in_stack] != bracket:
                    return False
        return len(brackets) == 0
                

        


        
