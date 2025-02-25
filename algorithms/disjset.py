class DisjSet:
    def __init__(self, n):
        # Constructor to create and initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.size = n

    # Finds set of given item x
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Do union of two sets represented by x and y.
    def Union(self, x, y):
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        self.size -= 1
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            if self.rank[xset] == self.rank[yset]:
                self.rank[yset] += 1

    #  Get the number of disjoint sets
    def getNumberOfSets(self):
        return self.size

    # Get all unique sets
    def getAllSets(self):
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets:
                sets[root] = []
            sets[root].append(i)
        return list(sets.values())
