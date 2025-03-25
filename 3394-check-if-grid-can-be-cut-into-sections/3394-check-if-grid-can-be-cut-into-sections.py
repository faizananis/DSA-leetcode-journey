class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        my_set=set()
        size=len(rectangles)
        for i in range(size):
            my_set.add(rectangles[i][0])
        if len(my_set)==size:
            return True
        my_set=set()
        for i in range(size):
            my_set.add(rectangles[i][1])
        if len(my_set)==size:
            return True
        my_set=set()
        for i in range(size):
            my_set.add(rectangles[i][2])
        if len(my_set)==size:
            return True
        my_set=set()
        for i in range(size):
            my_set.add(rectangles[i][3])
        if len(my_set)==size:
            return True
        return False
        