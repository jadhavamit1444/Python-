def Accept():

	size= int(input("Enter the number of elemnets"));
	arr=list();
	print("Enter the elements");
	
	for i in range(0,size,1):
		print("Enter number", i+1);
		a=int(input());
		arr.append(a);
		print(arr);

		print("Addition of elemnents", sum(map(int, arr)));




def main():
	Accept();
if __name__== "__main__":

	main();