class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority={}
        for n in nums:
            if n in majority:
                majority[n]+=1
            else:
                majority[n] = 1
        return max(majority, key=majority.get)


            