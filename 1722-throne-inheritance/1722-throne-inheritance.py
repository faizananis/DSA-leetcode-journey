class ThroneInheritance:
    def __init__(self, kingName):
        self.kingName = kingName 
        self.graph = defaultdict(list)
        self.ans = set()

    def birth(self, parentName, childName):
        self.graph[parentName].append(childName)

    def death(self, name):
        self.ans.add(name)

    def getInheritanceOrder(self):
        def function(node,parent):
            if node is None:
                return []

            res = [node]

            for neighbor in self.graph[node]:
                if neighbor != parent:
                    res += function(neighbor,node)

            return res 

        result = function(self.kingName,None)

        #return [i for i in result if i not in self.ans]
        res=[]
        for i in result:
            if i not in self.ans:
                res.append(i)
        return res



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()