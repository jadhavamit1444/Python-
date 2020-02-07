def patt():
    
    print("Enter the value");
    a=int(input());

    for i in range(a):
        for j in range(a):
            print('*',end=" ");
        print();
patt();
