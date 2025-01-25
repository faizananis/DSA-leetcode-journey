class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Step-1: Find location of each number
        copy = [(nums[i], i) for i in range(n)]

        # Step-2: Get ordered array with their original array index
        copy.sort()

        # Step-3: Find groups and place ordered values
        left, right = 0, 1
        while right < n:
            # Find group and get their original array indices
            pos = [copy[left][1]]
            while right < n and abs(copy[right][0] - copy[right - 1][0]) <= limit:
                pos.append(copy[right][1])
                right += 1

            # Order indices
            pos.sort()

            # Place ordered values to ordered indices in original array
            for i in range(right - left):
                nums[pos[i]] = copy[left + i][0]

            left = right
            right += 1
        
        return nums
