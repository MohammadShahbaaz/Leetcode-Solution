class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(1,numRows):
            pr = triangle[i-1]
            nr = [1]
            for j in range(len(pr)-1):
                nr.append(pr[j]+pr[j+1])
            nr.append(1)
            triangle.append(nr)
        return triangle
    

obj = Solution()

result = obj.generate(5)

for row in result:

    print(" " * (5 - len(row)), end="")

    for num in row:

        print(num, end=" ")

    print()