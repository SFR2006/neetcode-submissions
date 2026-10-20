class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    #just return the one number that doesn't appear multiple times
    #have o(n) --> so a loop and a o(1) so nothing heavy
        count={}
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1
        for n in count:   
            if count[n] == 1:
                return n


        