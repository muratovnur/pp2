class Solution(object):
    def largestAltitude(self, gain):
        att = [0]
        i = 1
        maxi = 0
        for x in gain:
            att.append(att[i-1] + x)
            if maxi < att[i]: 
                maxi = att[i]
            i += 1
        return maxi