class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        my_dict={}
        for i in range(len(answers)):
            if answers[i] in my_dict:
                my_dict[answers[i]]+=1
            else:
                my_dict[answers[i]]=1
        sums=0
        for n in my_dict:
            if n==0:
                sums+=my_dict[n]
            else:
                sums+=n+1
                if my_dict[n]>(n+1):
                    sums+=math.ceil(my_dict[n]/(n+1))
        return sums