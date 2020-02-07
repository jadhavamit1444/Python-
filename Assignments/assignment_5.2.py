def patt(n):
    if (n<1):
        return


    patt(n - 1);
    print(n, end=" ");



print("Enter the value");
n=int(input());
patt(n);




