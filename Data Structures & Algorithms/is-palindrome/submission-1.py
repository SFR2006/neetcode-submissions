class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        valid="abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        while l < r:
            while l < r and s[l] not in valid:
                l+=1
            while r > l and s[r] not in valid:
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r,=l+1,r-1
        return True
        
    

        