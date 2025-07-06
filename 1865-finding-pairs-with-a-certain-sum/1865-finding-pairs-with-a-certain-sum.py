class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1=nums1
        self.arr2=nums2

    def add(self, index: int, val: int) -> None:
        self.arr2[index]+=val

    def count(self, tot: int) -> int:
        n=0
        my_dict=Counter(self.arr2)
        for i in range(len(self.arr1)):
            if tot-self.arr1[i] in my_dict:
                n+=my_dict[tot-self.arr1[i]]
        return n


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)