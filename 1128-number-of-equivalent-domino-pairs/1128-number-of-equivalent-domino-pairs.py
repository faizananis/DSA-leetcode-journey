class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        arr=[0]*100
        result=0
        value=0
        for i in range(len(dominoes)):
            if dominoes[i][0]>dominoes[i][1]:
                dominoes[i][0],dominoes[i][1]=dominoes[i][1],dominoes[i][0]
            value=dominoes[i][0]*10+dominoes[i][1]
            arr[value]+=1
        for i in range(100):
            result+=arr[i]*(arr[i]-1)//2
        return result