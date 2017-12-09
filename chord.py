import random
class FingerTable:

	def __init__(self, nodeID):
		self.nodeID = nodeID
		self.table = [None,None,None,None,None,None,None,None,None]
		self.nodeTable = [None,None,None,None,None,None,None,None,None] #set of nodes (or 'fingers') which refer to other points on the ring

class Node:

	def __init__(self, nodeID):
		global nodeCount
		self.nodeID = nodeID
		nodeCount=nodeCount+1
		nodeList[nodeCount]=self

		self.table=FingerTable(nodeID)

		self.successor = None
		self.predecessor = None
		self.successorNode = None
		self.predecessorNode = None


	def printFingerTable(self):
		print "|                         Successor of key at",self.nodeID,"+2^i          |"
		print "|Finger Table at ", self.nodeID, ": " , self.table.table
		#if nodeCount == 1:
		#	print "(Since this is the first node in the topology, all of the fingers will point to its own ID.)"
	def printNodeStats(self):
		print "|NodeID = ", self.nodeID ,"                                                 |"
		print "|Successor = ", self.successor,"                                              |"
		print "|Predecessor = ", self.predecessor,"                                            |"
		print "|Successor NodeID = ", self.successorNode.nodeID, "                                       |"
		print "______________________________________________________________|"

def findSuccessor(node):
	pass


def printNodeCount():
	print "Node count = ", nodeCount

#called in the Node class __	__init__ function, it passes the node
def join(node):

	if nodeCount == 1:
		print "|This is the first node in the network.                       |"
		for x in range (1,9):
			node.table.table[x] = node.nodeID              #this makes the F.T. an array of the key n+2^i
			node.table.nodeTable[x] = node            #this makes the F.T. an array of nodes (just itself since this is the first node)	

			#need to set successor here

			node.successor=node.table.table[1]
			node.predecessor=node.table.table[1]	
			node.successorNode = node.table.nodeTable[1]	
			node.predecessorNode = node.table.nodeTable[1]


		#pass
	else:                               #join by giving it a random node in the topology. for beginning implementation we will continue to use the first node.		
		for x in range(1,9):
			node.table.table[x] = node.nodeID+(2**(x-1))   #this makes the F.T. an array of the key n+2^i
			node.table.nodeTable[x] = node            #this makes the F.T. an array of nodes (just itself currently)
			


			node.successor=node.table.table[1]
			node.predecessor=node.table.table[1]	
			node.successorNode = node.table.nodeTable[1]	
			node.predecessorNode = node.table.nodeTable[1]	

		#implement join here
		#pass
	
	printAllFingerTables()
	node.printNodeStats()

def printAllFingerTables():
	for x in range(1,nodeCount):
		nodeList[x].printFingerTable()
		#need to implement correct print function, pulling from nodeList[node]

#this is where the finger table is rebuilt after a node joins the ring
def rebuildFingerTables():
	pass
#return the successor of the key
def lookup(key):
	#enter in a node by 'external mechanism'. in this case, we will generate a random number between 0 and node count - 1 and take that node
	rndm = random.randint(1,nodeCount)
	refNode = nodeList[rndm]
	refNodeSuccessor = refNode.successor
	print "The random number generated is ", rndm, ".  The successor of the node at this index is ", refNodeSuccessor

#some global stuff
nodeList=[None,None,None,None,None]
nodeCount=0

print "***************************************************"
print ""
print "______________________________________________________________"

testNode = Node(5)
join(testNode)
lookup(1)
testNode2= Node(6)
join(testNode2)
lookup(1)

print ""
print ""
print "***************************************************"

