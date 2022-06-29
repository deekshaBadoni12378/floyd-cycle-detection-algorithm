class Node:
	def __init__(self, x):
		self.data = x
		self.next = None


head = None


def findLoop(head):
	sPointer = head
	fPointer = head

	while (sPointer != None
		and fPointer != None
		and fPointer.next != None):
		sPointer = sPointer.next
		fPointer = fPointer.next.next
		if (sPointer == fPointer):
			return 1

	return 0


head = Node(10)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)


temp = head
while (temp.next != None):
	temp = temp.next

temp.next = head


if (findLoop(head)):
	print("Loop exists")
else:
	print("Loop does not exist")


