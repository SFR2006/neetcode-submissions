class Solution:
    def romanToInt(self, s: str) -> int:
     #we are coverting strings that are roman numerials to actual numbers
     #we need to identify exactly what to do for problems when including like IV which means 4, when the smaller val comes before the larger it becomes negativr
     #is there a roman function or something
     #tiem(o(n)) space(o(1))

        roman={ "I":1, "X":10, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res=0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]: #checking if i in bounds
                res -= roman[s[i]]
            else:
                res +=roman[s[i]]
        return res