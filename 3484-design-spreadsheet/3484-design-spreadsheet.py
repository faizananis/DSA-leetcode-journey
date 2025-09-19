class Spreadsheet:

    def __init__(self, rows: int):
        self.table=[[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        ch=cell[0]
        col=ord(ch)-65
        val=int(cell[1:])
        row=val-1
        self.table[row][col]=value

    def resetCell(self, cell: str) -> None:
        ch=cell[0]
        col=ord(ch)-65
        val=int(cell[1:])
        row=val-1
        self.table[row][col]=0

    def getValue(self, formula: str) -> int:
        i=1
        row=0
        col=0
        res=0
        for _ in range(2):
            if formula[i].isalpha():
                ch=formula[i]
                col=ord(ch)-65
                i+=1
                num=0
                while i<len(formula) and formula[i]!='+':
                    num*=10
                    num+=ord(formula[i])-48
                    i+=1
                i+=1
                row=num-1
                res+=self.table[row][col]
            else:
                num=0
                while i<len(formula) and formula[i]!='+' :
                    num*=10
                    num+=ord(formula[i])-48
                    i+=1
                i+=1
                res+=num
        return res


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)