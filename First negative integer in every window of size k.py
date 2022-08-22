def printFirstNegativeInteger( A, N, K):
    # code here
    i,j=0,0
    res = []
    temp = []
    while(j<N):
        if A[j] < 0:
            temp.append(A[j])
        if (j - i + 1 < K):
            j += 1
        elif (j - i + 1 == K):
            if len(temp) > 0:
                res.append(temp[0])
                if A[i] in temp:
                    temp.pop(0)
                i += 1
                j += 1
            else:
                res.append(0)
                i += 1
                j += 1
    return res
