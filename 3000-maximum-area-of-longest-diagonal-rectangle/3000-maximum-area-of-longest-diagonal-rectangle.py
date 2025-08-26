class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag=0
        diag=0
        area=0
        max_area=0
        for i in range(len(dimensions)):
            diag=dimensions[i][0]**2+dimensions[i][1]**2
            area=dimensions[i][0]*dimensions[i][1]
            if diag>max_diag or (diag==max_diag and area>max_area):
                max_area=area
                max_diag=diag
            
        return max_area