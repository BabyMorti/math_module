pi = 3.141592   #pi number
tau = 6.283185   #tau number
e = 2.718281   #e number
inf = float('inf')   #infinity
nan = float('NaN')   #NaN

def description():   #description function
    '''Return description of this module'''
    version = '0.0.1'
    return '''This is a math module made by Gregor Zhilich.
    Version 0.0.1, Python 3.8.0'''
def gcd(a,b):   #gcd function
	'''Return the greatest common divisor of a and b'''
	if b==0:
		return a
	else:
		return gcd(b,a%b)
def lcm(a,b):   #lcm function
	'''Return the least common divisor of a and b'''
	res = (a * b) / gcd(a, b)
	return int(res)
def log(a, b):   #logarithm function
	'''Return the logarithm of a with base b'''
	res = 0
	while a!=1:
		a /= b
		res += 1
	return res
def factorial(a):   #factorial function
	'''Return the factorial of a'''
	res = 1
	for i in range(1, a+1):
		res *= i
	return res
def pow(a, b):   #power function
	'''Return a to the power of b'''
	res = 1
	for i in range(1, b+1):
		res *= a
	return res
def sqrt(a):   #square function
	'''Return the square root of a'''
	res = a ** 0.5
	if res.is_integer():
		return int(res)
	else:
		return round(res, 3)
def cbrt(a):   #cube root function
	'''Return the cube root of a'''
	res = a ** 0.33333
	return round(res, 3)
def abs(a):   #absolute value function
	'''Return the absolute value of a'''
	if a<0:
		return -a
	else:
		return a
def iter_sum(arr):   #function returns a sum of values in the iterable
	'''Return the sum of values in the iterable'''
	res = 0
	for i in arr:
		res += i
	return int(round(res, 0))
def copysign(a, b):   #function returns a with sign of b
	'''Return a with sign of b'''
	a = abs(a)
	if b < 0:
		res = -a
	else:
		res = a
	return res
def floor(a):
	'''Return the floor of a as an Integral'''
	res = int(round(a))
	if res > a:
		res-=1
	return res
def is_inf(a):   #test for infinity
	'''Returns True if your value is infinity'''
	if a != inf and a!=-inf:
		return False
	else:
		return True
def is_nan(a):   #test for NaN
	'''Returns True if your value is NaN'''
	if a != a:
		return True
	else:
		return False
def isfinite(a):
    '''Return True if x is neither an infinity nor a NaN'''
    if a==a and a!=inf and a!=-inf:
        return True
    else:
        return False
