class Solution:
    def matrixReshape(self, mat, r, c):
        a = sum(mat, [])
        return [a[i*c:(i+1)*c] for i in range(r)] if len(a) == r*c else mat