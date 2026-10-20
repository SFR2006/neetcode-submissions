class Solution:
     def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(map(str, digits)))

        digits += 1

        return [int(d) for d in str(digits)]