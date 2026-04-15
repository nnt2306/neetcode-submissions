class Solution:
    def isValid(self, s: str) -> bool:
       stack_brac = []
       brac_map = {'{':'}','[':']','(':')'}
       

       for i,brac in enumerate(s):
           if s[i] in brac_map:
              stack_brac.append(s[i])
           else:
             if not stack_brac: ## this handle case we have only close bracket
                return False
             elif brac_map[stack_brac.pop()] != s[i]: 
                ## If the first close bracket does not match with the most recent open 
                ## we return False directly
                return False
        
       if not stack_brac: ## Later if we have empty list we will return True
           return True
       else: ## Other wise we still have open bracket left like "(" we return False
           return False
        
       ## The ideal of the stack is the LIFO structure so allow us to check
       ## efficiently the most recent open and close
           
              
