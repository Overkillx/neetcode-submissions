class Solution:
    def isPalindrome(self, s: str) -> bool:
        req_str=""
        low= "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in range (len(s)):
            if(s[i].lower() in low):
                req_str += s[i].lower()
        if (req_str[::-1] == req_str):
            return True
        else:
            return False    

        