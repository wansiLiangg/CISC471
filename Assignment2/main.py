'''
CISC 471 HW2
'''

#Part1 -- Programming
#Question 1.1 Find an Eulerian Cycle in a Graph
class LinkedList:
    def __init__(self, node):
        self.node = node
        self.next = self

    def insert(self, link):
        link.next = self.next
        self.next = link
        return link

def eulerianCycle(graph):
    cloneGraph = graph.copy()
    node = next(node for node, neighbour in cloneGraph.items() if neighbour)    #Get a node that has edges
    neighbours = cloneGraph[node]
    start = currentNode = LinkedList(node)
    visited = {}
    while True:
        cycleStart = node
        while neighbours != []:
            visited[node] = currentNode
            node = neighbours.pop()
            neighbours = cloneGraph[node]
            currentNode = currentNode.insert(LinkedList(node))
        if node != cycleStart:
            return "No Eulerian cycle"

        #A visited node still has edges
        while visited != {}:
            node, currentNode = visited.popitem()
            neighbours = cloneGraph[node]
            if neighbours != []:
                break
        else:
            break
    if cloneGraph.values() == []:
        return "No Eulerian cycle"
    eulerianCycle = []
    currentNode = start
    while True:
        eulerianCycle.append(currentNode.node)
        currentNode = currentNode.next
        if currentNode == start:
            break
    return eulerianCycle

#Question 1.2 Generate Contigs from a Collection of Reads
def generateContigs(reads):
    prefixs = {}
    suffixs = {}
    k1mer = []
    k = len(reads[0])
    for seg in reads:
        prefix = seg[:-1]
        suffix = seg[1:]
        if prefix not in k1mer:
            k1mer.append(prefix)
        if suffix not in k1mer:
            k1mer.append(suffix)

    #Add k-1mer prefix and suffix as keys to the dictionaries
    for i in k1mer:
        prefixs[i] = []
        suffixs[i] = []

    #When the key is the prefix to the element, add k-1mer suffix to the dictionary
    for seg in reads:
        prefixs[seg[:-1]].append(seg[1:])

    #When the key is the suffix to the element, add k-1mer prefix to the dictionary
    for key in prefixs.keys():
        temp = prefixs[key]
        for j in temp:
            if j in suffixs.keys():
                suffixs[j].append(key)
            else:
                suffixs[j] = [key]

    #Generate contigs
    contig = ""
    for key in prefixs.keys():
        if prefixs[key] != [] and len(prefixs[key]) != 1 or len(suffixs[key]) != 1:
            for k in prefixs[key]:
                contig = key[:] + k[-1]
                if prefixs[k] != []:
                    if len(prefixs[k]) != 1 or len(suffixs[k]) != 1:
                        print(contig)
                        continue
                    else:
                        x = prefixs[k][0]
                        contig = contig + x[-1]
                        while prefixs[x] != [] and len(prefixs[x]) == 1 and len(suffixs[x]) == 1:
                            contig = contig + prefixs[x][0][-1]
                        print(contig)
                else:
                    print(contig)
                    continue

#Unit tests for part1
#Inputs for Eulerian Cycle
graph1 = {"0":["3"], "1":["0"], "2":["1","6"], "3":["2"], "4":["2"], "5":["4"], "6":["5","8"], "7":["9"], "8":["7"], "9":["6"]}
graph2 = {"A":["E","F"], "B":["A"], "C":["A","B"], "D":["C"], "E":["C", "D"], "F":["E"]}
graph3 = {"A":["B","C"], "B":["C", "E"], "C":["D"], "D":["B"], "E":["D"]}

#Inputs for generate contigs
contig1 = ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"]
contig2 = ["ATG", "TTG", "TGA", "ACA", "GAT", "TGA", "ATT", "GAC"]
contig3 = ["ATG", "ATG", "TGT", "TGA", "CAT", "GGA", "GAT", "AGA"]

def main():
    print("Positive unit test of Eulerian Cycle")
    print(eulerianCycle(graph1))

    print("Positive unit test of Eulerian Cycle")
    print(eulerianCycle(graph2))

    print("Negative unit test of Eulerian Cycle")
    print(eulerianCycle(graph3))

    print("")

    print("Positive unit test of generate contigs")
    generateContigs(contig1)

    print("Positive unit test of generate contigs")
    generateContigs(contig2)

    print("Negative unit test of generate contigs")
    generateContigs(contig3)

main()
