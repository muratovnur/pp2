class Solution(object):
    def subtractProductAndSum(self, n):
        n = str(n) # convert to String
        nsum = 0 # initial value 
        nproduct = 1 # initial value(if we do zero product would always be zero so 1 is the right value)
        for x in n:
            nsum += int(x) # Convert to integer 
            nproduct *= int(x) # convert to integer . 
        return nproduct - nsum
a = Solution()
print(a.subtractProductAndSum(4421))