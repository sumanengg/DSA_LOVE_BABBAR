#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        def pair(s1, s2):
            i, j = 0, 0
            comm = ""
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    comm += s1[i]
                    i += 1
                    j += 1
                else:
                    break
            return comm
        
        if  n == 0:
            return -1
        if n == 1:
            return arr[0]
        lcp = arr[0]
        for i in range(1,n):
            lcp = pair(lcp, arr[i])
            if lcp == "":
                return -1
        return lcp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
