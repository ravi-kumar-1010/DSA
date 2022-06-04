class Solution:
    def merge(self, X, Y):
        i = j = 0
        out = []
        while(i < len(X) and j < len(Y)):
            if X[i] < Y[j]:
                out.append(X[i])
                i +=1
            else:
                out.append(Y[j])
                j +=1
        if i < len(X):
            for Xleft in range(i,len(X)):
                out.append(X[Xleft])
        if j < len(Y):
            for Yleft in range(j,len(Y)):
                out.append(Y[Yleft])
        out.reverse()
        return out


if __name__ == "__main__":
    ob = Solution()
    X = [1, 3, 5, 7, 8]
    Y = [2, 4, 6, 9]
    out = ob.merge(X,Y)
    print(out)
    
