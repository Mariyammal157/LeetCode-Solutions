class Solution:
    def findRelativeRanks(self, score):
        a = sorted(score, reverse=True)
        d = {x: i+1 for i, x in enumerate(a)}
        return ["Gold Medal" if d[x]==1 else "Silver Medal" if d[x]==2 else "Bronze Medal" if d[x]==3 else str(d[x]) for x in score]
        