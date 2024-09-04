# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         i=0
#         totalSum=0
#         size=len(chalk)
#         while i<size:
#             totalSum=totalSum+chalk[i]
#             i+=1
#         # num=totalSum % k
#         # while i<len(chalk):
#         #     num-=chalk[i]
#         #     if num<0:
#         #         return i
        #     i+=1
# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         total_chalk = sum(chalk)  # 2nd Example
#         k = k % total_chalk       # 25%10  =  k = 5 
#         i = 0
#         while k >= chalk[i]:      # -2>=1   
#             k -= chalk[i]         # k=k-chalk[i]  # k=5-3  = 2  # i=0
#                                   # k=2-4  = -2 # i=1
#             i += 1
#         return i
class Solution:
     def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalks=sum(chalk)
        k=k%total_chalks
        i=0
        while k>=0:
            k-=chalk[i]
            if k<=0:
                return i
            i+=1