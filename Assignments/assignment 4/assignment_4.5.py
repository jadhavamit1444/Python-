import math
from math import sqrt
from functools import *

def accept():
	size=int(input("Enter the number of elements"));
	arr=list();

	print("Enter the element");
	for i in range(0,size):
		print("Enter elements", i+1);
		a=int(input());
		arr.append(a);
		print("LIST=", arr);

	return arr;

def chkprime(a):
	for i in range(2, int(math.sqrt(a)) + 1):
		if a % i == 0:
			return False
	return True

def modify(a):
	return a*2;

def maxi(a1,a2):
	return max(a1,a2);



def main():
	demo=accept();

	xyz=list(filter(chkprime,demo));
	print("LIST AFTER FILTER", xyz);

	pqr=list(map(modify, xyz));
	print("LIST AFTER MAP", pqr);

	abc= reduce(maxi, pqr);
	print("FINAL LIST", abc );

if __name__== "__main__":
	main();
