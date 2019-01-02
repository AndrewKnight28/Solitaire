class Stack:

	def __init__(self):
		self.top = self.size = 0
		self.S = []

	def isEmpty(self):
		return self.size == 0

	def push(self, data):
		self.S.append(data)
		self.top = self.size
		self.size = self.size + 1

	def pop(self):
		if self.isEmpty():
			print("Empty")
			return
		del self.S[self.top]
		self.size = self.top
		self.top = self.top - 1 

	#def show_top(self):
	#	if self.isEmpty():
	#		print("Stack is empty")
	#	print("Top item is",  self.S[self.top]) 	
