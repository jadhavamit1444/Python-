def patt(n):
    if (n<1):
        return


    print('*', end=" ");
    patt(n-1);


print("Enter the value");
n=int(input());
patt(n);




