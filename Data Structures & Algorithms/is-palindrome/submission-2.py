class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all spaces
        ## s.split() returns a list of substrings/words
        ## s.strip() will remove the space at the end and the begining
        ## s.replace(" ","") remove all space
        ## s.translate(str.maketrans()) will remove simultaneously characters
        ##.isalpha is check whether a string consists only of alphabetic letters and is non-empty
        ##.lower is 
        clean_s = "".join(ch.lower() for ch in s if ch.isalpha() or ch.isdigit())    
        start = 0
        end = len(clean_s)-1

        

        while start < end:
            if clean_s[start] == clean_s[end]:
                start +=1
                end -=1
            else:
                return False
        return True