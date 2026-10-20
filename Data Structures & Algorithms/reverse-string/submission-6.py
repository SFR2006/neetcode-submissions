class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #taking each value and then swapping, two pointer, left and right
        #time O(n) (iterating throug entire list) # space O(1)
        l,r=0,len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l] #reassiging each val, swapping 
            l+=1 #updating pointers
            r-=1
        #dont need to return anything modifing in place

    #solution version 2: mem:o(n) --> stacks efficient, but takes more space
    #put everything into a stack and then pop out one by one

    #stack=[]
    #for c in s:
        #stack.append(c)
    #i=0
    #while stack:
        #s[i]=stack.pop()
        #i+=1

    #solution version 3: recursive
    #   def reverse(l,r):
    #       if l < r:
    #            s[l],s[r],=s[r],s[l]
    #            reverse(l+1,r-1)
    #   reverse(0,len(s)-1)

        