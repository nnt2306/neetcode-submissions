class Solution:
    def isValid(self, s: str) -> bool:
       stack_brac = []
       brac_map = {'{':'}','[':']','(':')'}
       if len(s) ==1:
          return False
       for i,brac in enumerate(s):
           if s[i] in brac_map:
              stack_brac.append(s[i])
           else:
             if not stack_brac:
                return False
             elif brac_map[stack_brac.pop()] != s[i]:
                return False
        
       if not stack_brac:
           return True
       else:
           return False

           
              
