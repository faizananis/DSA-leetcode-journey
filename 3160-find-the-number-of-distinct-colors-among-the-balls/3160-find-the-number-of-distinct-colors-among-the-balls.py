class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        my_dict={}
        my_set=set()
        result=[0]*len(queries)
        for i in range(len(queries)):
            if queries[i][0] in my_dict:
                my_set.remove(my_dict[queries[i][0]])
            my_dict[queries[i][0]]=queries[i][1]
            my_set.add(queries[i][1])
            result[i]=len(my_set)
        return result