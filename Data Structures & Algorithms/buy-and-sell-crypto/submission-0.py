
#essentially in this project weare trying to select the smallest number for i for first (what we are buying) andd then we find the next biggest number (what we are selling), we then subtract the difference between the two and thats how we would get the max return, if all the big numbers come before the small numbers we cannot get a profitable return and thus would return nothing--sliding windo problem --> buy low sell high

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        buy = prices[0]
        profit = 0

        for p in prices:
            if p < buy:
                buy = p

            if p - buy > profit:
                profit = p - buy

        return profit
    