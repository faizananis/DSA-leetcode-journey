class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict=defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            my_dict[key].append(s)
        
        return list(my_dict.values())


        # while count<len(s)
        # for s in strs:
        #     res.append(s)
        #     temp=sorted(s)
        #     if temp in my_dict:
        #         res.append(my_dict[temp])
        #         del my_dict[temp]
        #     else:
        #         my_dict[temp]=s
        