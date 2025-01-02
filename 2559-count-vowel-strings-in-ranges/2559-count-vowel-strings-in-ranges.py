class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels=set(['a','e','i','o','u'])
        n=len(words)
        prefix_sum=[0]*(n+1)
        count=0
        result=[]
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count+=1
            prefix_sum[i+1]=count
        for q in queries:
            result.append(prefix_sum[q[1]+1]-prefix_sum[q[0]])
        return result

