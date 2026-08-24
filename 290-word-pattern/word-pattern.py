class Solution:
    def wordPattern(self, pattern, s):
        a = pattern
        b = s.split()
        return len(a) == len(b) and len(set(zip(a,b))) == len(set(a)) == len(set(b))