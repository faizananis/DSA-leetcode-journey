class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        my_set={'a','e','i','o','u'}
        res=[]
        for query in queries:
            check=False
            if query in wordlist:
                res.append(query)
                continue
            for word in wordlist:
                if len(word)!=len(query):
                    continue
                for i in range(len(word)):
                    if word[i]==query[i]:
                        continue
                    if abs(ord(word[i])-ord(query[i]))==32:
                        continue
                    if word[i] in my_set and query[i] in my_set:
                        continue
                    break
                else:
                    res.append(word)
                    check=True
                    break
            else:
                if not check:
                    res.append("")
        return res
            
                    


