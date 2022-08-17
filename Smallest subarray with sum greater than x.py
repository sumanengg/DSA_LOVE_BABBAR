class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        l,total = 0,0
        res = float("inf")
        for r in range(n):
            total += a[r]
            while total > x:
                res = min(r - l + 1,res)
                total -= a[l]
                l += 1
        return res  
