class Solution(object):
    def getRow(self, rowIndex):
        triangle = [1]
        for i in range(1,rowIndex+1):
            nr = [1]
            for j in range(len(triangle)-1):
                nr.append(triangle[j]+triangle[j+1])
            nr.append(1)
            triangle = nr
        return triangle