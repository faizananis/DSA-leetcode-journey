class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict=defaultdict(list)
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                key=i+j
                my_dict[key].append(mat[i][j])
        my_list=list(my_dict.values())
        print(my_list)
        res=[]
        for i in range(len(my_list)):
            if i%2==1:
                res.extend(my_list[i])
            else:
                res.extend(reversed(my_list[i]))
        return res
                