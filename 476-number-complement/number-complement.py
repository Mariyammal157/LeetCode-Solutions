class Solution:
    def findComplement(self, num):
        b = bin(num)[2:]
        return int(''.join('1' if x == '0' else '0' for x in b), 2)
        