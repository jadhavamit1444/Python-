
def factorial(n):

    return 1 if (n==0 or n==1) else n*factorial(n-1);

print("Enter the value");
a=int(input());

print("Factorial of", a, "is", factorial(a));
