class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white=0
        left=0
        minWhite=len(blocks)
        for i in range(k):
            if blocks[i]=='W':
                white+=1
        minWhite=min(minWhite,white)
        for right in range(k,len(blocks)):
            if blocks[left]=='W':
                white-=1
            if blocks[right]=='W':
                white+=1
            left+=1
            minWhite=min(minWhite,white)
        return minWhite
        
            
            
            
            