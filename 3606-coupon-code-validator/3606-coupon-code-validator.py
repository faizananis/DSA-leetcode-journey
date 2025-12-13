class Solution:
    def isalphanumeric(self, st):
        return all(c.isalnum() or c=='_' for c in st)

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        my_dict={"electronics","grocery","pharmacy","restaurant"}
        ans=[]
        for i in range(len(code)):
            if code[i]=="":
                continue
            if not self.isalphanumeric(code[i]):
                continue
            if not businessLine[i] in my_dict:
                continue
            if isActive[i] == False:
                continue
            ans.append([businessLine[i],code[i]])
        ans.sort()
        values=[]
        for i in range(len(ans)):
            values.append(ans[i][1])
        return values