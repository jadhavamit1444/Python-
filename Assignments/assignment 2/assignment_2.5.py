def prime():
	print("Enter the Number");
	a=int(input());

	if a > 1:

    		for i in range(2, a):
        		if (a % i) == 0:
            			print(a, "it is not a prime number")

            			break
    		else:
        		print(a, "it is a prime number");
	else:
         print(a, "it is not a prime number");

prime();