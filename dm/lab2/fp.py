from itertools import chain, combinations
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      
        self.children = {}   
    def inc(self, numOccur):
        self.count += numOccur       
    # def disp(self, ind=1):
    #     print ('  '*ind, self.name, ' ', self.count)
    #     for child in self.children.values():
    #         child.disp(ind+1)
def createTree(dataSet, minSup=1): 
    # print(minSup)
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # print(headerTable)
    for k in list(headerTable): 
        if headerTable[k] < minSup: 
            del(headerTable[k])
    # print(headerTable)
    freqItemSet = set(headerTable.keys())
    # print(freqItemSet)
    if len(freqItemSet) == 0: return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] 
    retTree = treeNode('Null Set', 1, None) 
    for tranSet, count in dataSet.items(): 
        localD = {}
        for item in tranSet: 
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable 
def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:  
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
def updateHeader(nodeToTest, targetNode):   
    while (nodeToTest.nodeLink != None):   
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
def loadSimpDat(fname):
    output=[]
    file = open(fname, 'r')
    for line in file:
        line = line.strip().rstrip(',')                         
        record = list(line.split(','))
        output.append(record)
    # print(output[:5])
    return output
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
def ascendTree(leafNode, prefixPath): 
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
def findPrefixPath(basePat, treeNode): 
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def Mine_Tree(FPTree, HeaderTable, minSupport, prefix, frequent_itemset):
    bigL = [v[0] for v in sorted(HeaderTable.items(),key=lambda p: p[1][0])]
    for basePat in bigL:
        new_frequentset = prefix.copy()
        new_frequentset.add(basePat)
        frequent_itemset.append(new_frequentset)
        Conditional_pattern_bases = findPrefixPath(basePat, HeaderTable[basePat][1])
        Conditional_FPTree, Conditional_header = createTree(Conditional_pattern_bases,minSupport)

        if Conditional_header != None:
            Mine_Tree(Conditional_FPTree, Conditional_header, minSupport, new_frequentset, frequent_itemset)



def main():
    q = int(input("1.Test Data\t2. Retail Data\nChoice: "))
    p = "test_dataset_1.csv"
    if q==2:
        p = "retail_dataset.csv"
    # print(p)
    simpDat = loadSimpDat(p)
    initSet = createInitSet(simpDat)
    minsup=int(input("Enter the minimum support:"))
    minconf=float(input("Enter the minimum confidence:"))
    myFPtree, myHeaderTab = createTree(initSet, minsup)
    # frequent_itemset = None 
    # myFPtree.disp()
    frequent_itemset = []
    Mine_Tree(myFPtree, myHeaderTab, minsup, set([]), frequent_itemset)
    # print(findPrefixPath('I1', myHeaderTab['I1'][1]))
    # print(findPrefixPath('I2', myHeaderTab['I2'][1]))
    # print(findPrefixPath('I3', myHeaderTab['I3'][1]))
    # print(findPrefixPath('I4', myHeaderTab['I4'][1]))
    # print(findPrefixPath('I5', myHeaderTab['I5'][1]))
    # print(assoc(frequent_itemset,minconf))
    print("Frequent itemsets:",frequent_itemset)

if __name__ == '__main__':
    main()