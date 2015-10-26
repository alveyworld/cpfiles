# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Functions
def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c

def ratio(f1, f2):
	if f1 > f2:
		return f1 / f2
	else:
		return f2 / f1

def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainder(40, 19): ", remainder(40, 19)
	print "test remainder(126, 19): ", remainder(126, 19)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "testing ratio(7.7, 2.8): ", ratio(7.7, 2.8)
	print "testing ratio(2.8, 7.7): ", ratio(2.8, 7.7)
	print "testing pythagoras(3, 4): ", pythagoras(3, 4)
	print "testing pythagoras(28, 32): ", pythagoras(28, 32) 


def reverse(jimmy):
	return not jimmy
	
def band(bool1, bool2):
	return bool1 and bool2

def bor(bool1, bool2):
	return bool1 or bool2

def xsame(bool1, bool2):
	return bool1 == bool2

def xor(bool1, bool2):
	return bool1 != bool2
	


def main_boolean():
	print "testing reverse(True): ", reverse(True)
	print "testing reverse(False): ", reverse(False)
	print "testing band(True, True): ", band(True, True)
	print "testing band(True, False): ", band(True, False)
	print "testing band(False, True): ", band(False, True)
	print "testing band(False, False): ", band(False, False)
	print "testing bor(True, True): ", bor(True, True)
	print "testing bor(True, False): ", bor(True, False)
	print "testing bor(False, True): ", bor(False, True)
	print "testing bor(False, False): ", bor(False, False)
	print "test xsame(True, True): ", xsame(True, True)
	print "test xsame(False, False): ", xsame(False, False)
	print "test xsame(True, False): ", xsame(True, False)
	print "test xsame(False, True): ", xsame(False, True)
	print "test xor(True, True): ", xor(True, True)
	print "test xor(False, False): ", xor(False, False)
	print "test xor(True, False): ", xor(True, False)
	print "test xor(False, True): ", xor(False, True)
	
def positive(n):
	return n > 0
		
def bigger(x, y):
	return x > y

def no_diff(d, b):
	return d == b
	

def main_boolean_numbers():
	print "testing positive(-29): ", positive(-29)
	print "testing positive(29): ", positive(29)
	print "test bigger(3, 2): ", bigger(3, 2)
	print "test bigger(7, 14): ", bigger(7, 14)
	print "testing no_diff(45, 82): ", no_diff(45, 82)
	print "testing no_diff(77, 77): ", no_diff(77, 77)
	
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	main_boolean_numbers()
	
main()