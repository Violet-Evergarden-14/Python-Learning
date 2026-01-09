class A:
	def __init__(self):
		print(0)

class B1(A):
	def __init__(self):
		super().__init__()
		print(1)

class B2(A):
	def __init__(self):
		super().__init__()
		print(2)

class C(B1, B2):
	def __init__(self):
		super().__init__()
		print(3)

c = C()
print(C.mro())

"""class A:
	def __init__(self, x, y):
		self.x = x   #必须写self.
		self.y = y

	def add(self):
		return self.x + self.y

a = A(2, 3)   #注意参数写在创建时
m = a.add()
print(m)		
		
class B(A):
	def __init__(self, x, y, z):
		A.__init__(self, x, y)
		self.z = z

	def add(self):
		return A.add(self) + self.z

b = B(1, 2, 3)
m = b.add()
print(m)
"""

"""
class A:
	x = 1
	def hello(self):
		print("hello world")

class B:
	y = 2
	def Hello(self):
		print("Hello World")

class C(A, B):   #同样参数，从左到右找
	z = 3
	def HELLO(self):
		print("HELLO WORLD")
"""

"""
class A:
	def say(self):
		print("A")

class B:
	def say(self):
		print("B")

class C:
	def say(self):
		print("C")

class Table:
	a = A()
	b = B()
	c = C()
	def say(self):
		self.a.say()
		self.b.say()
		self.c.say()

t = Table()
t.say()
"""