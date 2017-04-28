import time
import random

def printArg(f):
	def argument( * arg ):
		print "Name: " + str(f.func_name) + " | Args: " + str(arg)
		return f( * arg)
	return argument 

def timer(f):
	def inner( * arg):
		a = time.time()
		val = f( * arg)
		b = time.time()
		print "Execution Time: " + str(b - a)
		#return f( * arg)
	return inner

@timer
@printArg 
def dumpling(x):
	print "I eat " + str(x) + " dumplings per day."
	return 

'''
TEST
Name: dumpling | Args: (1,)
I eat 1 dumplings per day.
Execution Time: 3.79085540771e-05
'''

@timer
@printArg 
def randomFood():
	foods = ["sushi","pizza","fries","rice","pasta","dumplings","cake"]
	print "Today you will eat " + random.choice(foods) 
	return

'''
TEST
Name: randomFood | Args: ()
Today you will eat dumplings
Execution Time: 4.29153442383e-05
'''