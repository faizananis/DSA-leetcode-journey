class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        range_min = float('inf')
        range_max = float('-inf')

        count = 0
        right = 0

        for right in range(n):
            range_min = min(range_min, nums[right])
            range_max = max(range_max, nums[right])

            if range_max - range_min > 2:
                win_size = right - left
                count += (win_size * (win_size + 1)) // 2

                left = right
                # Expand current window to as left as possible
                range_min = nums[right]
                range_max = nums[right]
                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    range_min = min(range_min, nums[left])
                    range_max = max(range_max, nums[left])

                # Subtract overcounted subarrays
                if left < right:
                    win_size = right - left
                    count -= (win_size * (win_size + 1)) // 2

        # Add subarrays from the last window
        win_size = right - left + 1
        count += (win_size * (win_size + 1)) // 2

        return count





        # maxi=-float("inf")
        # mini=float("inf")
        # count=0
        # left=0
        # right=0
        # while right<len(nums):
        #     maxi=max(maxi,nums[right])
        #     mini=min(mini,nums[right])
        #     if abs(max(maxi,nums[right]) - min(mini,nums[right]))>2:
        #         maxi=mini=nums[right]
        #         n=right-left
        #         count=count+(n*(n+1)//2)
        #         left=right
        #         while abs(max(maxi,nums[left]) - min(mini,nums[left]))<=2:
        #             maxi=max(maxi,nums[left])
        #             mini=min(mini,nums[left])
        #             left-=1
        #         n=right-left
        #         #count=count-(n*(n+1)//2)
        #         right=left
        #     right+=1
        # return count


