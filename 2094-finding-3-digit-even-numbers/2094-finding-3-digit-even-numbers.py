class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        my_dict=Counter(digits)
        result=[]
        for i in range(100,1000):
            num=i
            freq={}
            while num:
                if num%10 in freq:
                    freq[num%10]+=1
                else:
                    freq[num%10]=1
                num//=10
            for val in freq:
                if val in my_dict:
                    if my_dict[val]>=freq[val]:
                        continue
                break
            else:
                if not i&1:
                    result.append(i)
        return result
