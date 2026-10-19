

#so we have to loop through each list and add our a letter to each word if each word in the list has that letter if it doesn't we quit, basically we have to loop through one list and then loop through each item in the list to check
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if not strs:
            return prefix

        for i in range(len(strs[0])):
            letter = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return prefix

            prefix += letter

        return prefix

            
    
        return empty
