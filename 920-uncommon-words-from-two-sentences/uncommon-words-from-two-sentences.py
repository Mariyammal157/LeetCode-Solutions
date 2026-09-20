class Solution:
    def uncommonFromSentences(self, s1, s2):
        from collections import Counter
        c = Counter((s1 + " " + s2).split())
        return [x for x in c if c[x] == 1]
        