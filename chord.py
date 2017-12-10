import random
class FingerTable:

	def __init__(self, nodeID):
		self.nodeID = nodeID
		self.table = [None,None,None,None,None,None,None,None,None]     #array of key (n+2^(i-1))%256
		self.nodeTable = [None,None,None,None,None,None,None,None,None] #the successor of key at self.table[i]

class Node:

	def __init__(self, nodeID):
		global nodeCount
		self.nodeID = nodeID
		nodeCount=nodeCount+1
		nodeList[nodeCount]=self
		self.table=FingerTable(nodeID)
		for x in range(1,9):
			self.table.table[x] = (self.nodeID+(2**(x-1)))%256             #this makes the keytable an array of the key n+(2^(i-1))%256
		self.successor = None
		self.predecessor = None
		self.successorNode = None
		self.predecessorNode = None

	def printKeyTable(self):

		print "|Key Table at ", self.nodeID, ": " , self.table.table 
		print "|                         Successor of key at",self.nodeID,"+2^i          |"  
		print "______________________________________________________________|"
	
	def printNodeStats(self):
		print "|NodeID = ", self.nodeID ,"                                                 |"
		print "|Predecessor NodeID = ", self.predecessorNode.nodeID, "                                     |"
		print "|Successor NodeID = ", self.successorNode.nodeID, "                                       |"

	def isInRange(num1, num2):
		if self.nodeID>=num1 and self.nodeID<num2:
			return true
		else:
			return false





	#goal: pass the new incoming node into the function, return its successor
	def findSuccessor(newNode):
	
		#if newNode.isInRange(self.table.table[1], self.table.table[2]):






		pass

	def findPredecessor(newNode):
		pass

	def findClosestPrecedingFinger(newNode):
		
		






		pass

def printNodeCount():
	print "Node count = ", nodeCount

def initializeFingerTable(node):
	pass

#called in the Node class __	__init__ function, it passes the node
def join(node):

	if nodeCount == 1:
		print "|          This is the first node in the network.             |"
		for x in range (1,9):
			node.table.nodeTable[x] = node      #this makes the F.T. an array of nodes (just itself since this is the first node)		
		node.successorNode = node.table.nodeTable[1]
		node.predecessorNode = node.table.nodeTable[1]
	else: #join by giving it a random node in the topology. for beginning implementation we will continue to use the first node.		
		for x in range(1,9):
			#to change
			
			#initializeFingerTable(node)


			node.table.nodeTable[x] = node            #this makes the F.T. an array of nodes (just itself currently)
			node.successorNode = node.table.nodeTable[1]	
			node.predecessorNode = node.table.nodeTable[1]	




			#pass
		#implement join here

	
	printAllFingerTables()
	node.printNodeStats()

def printAllFingerTables():
	for x in range(1,nodeCount):
		nodeList[x].printKeyTable()
		#need to implement correct print function, pulling from nodeList[node]

#this is where the finger table is rebuilt after a node joins the ring
#want to do something as many times as there are nodes (nodeCount)
def rebuildFingerTables():
	pass

def stabilize():
	pass



#return the successor of the key
def lookup(key):
	#enter in a node by 'external mechanism'. in this case, we will generate a random number between 0 and node count - 1 and take that node
	if nodeCount==1: 
		rndm = random.randint(1,nodeCount) 
		refNode = nodeList[rndm]
		refNodeSuccessor = refNode.successorNode.nodeID
		print "The random number generated is ", rndm, ".  The successor of the node at this index is ", refNodeSuccessor
	else:
		rndm = random.randint(1,nodeCount-1) #want to exclude the last added node 
		refNode = nodeList[rndm]
		refNodeSuccessor = refNode.successorNode.nodeID
		print "The random number generated is ", rndm, ".  The successor of the node at this index is ", refNodeSuccessor	

#some global stuff
nodeList=[None,None,None,None,None]
nodeCount=0

print "***************************************************"
print ""
print "______________________________________________________________"

testNode = Node(5)
join(testNode)

testNode2= Node(6)
join(testNode2)
lookup(1)

print ""
print ""
print "***************************************************"

