class Solution(object):
    def interpret(self, command):
        x = command.replace('()', 'o')
        z = x.replace('(al)', 'al')
        return z
a = Solution()
print(a.interpret("(al)G(al)()()G"))