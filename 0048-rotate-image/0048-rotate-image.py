class Solution:
    # def reverse(self,arr):
    #     i=0
    #     j=len(arr)-1
    #     while i<j:
    #         arr[i],arr[j]=arr[j],arr[i]
    #         i+=1
    #         j-=1
    #     return arr

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            # arr=self.reverse(matrix[i])
            matrix[i].reverse()
        
        
