
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

def chkeven(a):
	if a%2==0:
		return True;
	else:
		return False;

def modify(a):
	return a*a;

def add(a1,a2):
	return a1+a2;



def main():
	demo=accept();

	xyz=list(filter(chkeven,demo));
	print("LIST AFTER FILTER", xyz);

	pqr=list(map(modify, xyz));
	print("LIST AFTER MAP", pqr);

	abc= reduce(add, pqr);
	print("FINAL LIST", abc );

if __name__== "__main__":
	main();
