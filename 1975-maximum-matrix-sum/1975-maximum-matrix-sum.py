class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        min_val = float('inf')
        count_neg = 0
        total_sum = 0

        for i in range(m):
            for j in range(n):
                total_sum += abs(matrix[i][j])
                min_val = min(min_val, abs(matrix[i][j]))

                if matrix[i][j] < 0:
                    count_neg += 1

        if count_neg % 2 == 0:
            return total_sum
        return total_sum - 2 * min_val




        # m=len(matrix)
        # n=len(matrix[0])
        # count=0
        # minimum=10000000
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             break
        #         if matrix[i][j]<0:
        #             count+=1
        #     else:
        #         continue
        #     break
        # else:
        #     if count%2==1:
        #         for i in range(m):
        #             for j in range(n):
        #                 minimum=min(minimum,matrix[j][j])
        # sums=0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]<0:
        #             sums+=-matrix[i][j]
        #         else:
        #             sums+=matrix[i][j]
        # if minimum!=10000000:
        #     sums-=minimum
        # return sums

