class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char

        for i in range(len(cleaned) // 2):
            if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
                return False

        return True
        