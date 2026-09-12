class Solution:
    def findWords(self, words):
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        return [w for w in words if any(set(w.lower()) <= set(r) for r in rows)]