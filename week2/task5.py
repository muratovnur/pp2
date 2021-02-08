class Solution(object):
    def subtractProductAndSum(self, n):
        n = str(n)
        nsum = 0
        nproduct = 1
        for x in n:
            nsum += int(x)
            nproduct *= int(x)
        return nproduct - nsum