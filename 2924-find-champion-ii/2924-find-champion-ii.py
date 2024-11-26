class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        my_list=[0]*n
        for i in range(len(edges)):
            my_list[edges[i][1]]+=1

        unique_count=0
        unique_value=0
        for i in range(n):
            if my_list[i]==0:
                unique_count+=1
                unique_value=i
        
        if unique_count>1:
            return -1
        return unique_value