
class Numbers:

    def __init__(self, value):
        self.value=value;

    def chkprime(self):
        self.chk=0;
        for i in range(2, (self.value//2 +1)):
            if (self.value %i==0):
                self.chk=self.chk+1;
                break;
        if (self.chk==0 and self.value!=1):
            print(" it is prime number");
        else:
            print("it is not prime number");


    def chkperfect(self):
        self.sum=0;
        for i in range(1, self.value):
            if (self.value%i==0):
                self.sum=self.sum+i;

        if (self.sum==self.value):
            print("It is a perfect number");
        else:
            print("not a perfect number");



    def factors(self):
        for i in range(1, self.value + 1):
            if (self.value % i==0):
                print(i);

    def sumoffactors(self):
        self.add=0;
        for i in range(1, self.value+1):
            self.add=self.add+i;
            print(self.add);




def main():
    obj1=Numbers(int(input("Enter the value")));

    obj1.chkprime();

    obj1.chkperfect();

    print("Factors of number");
    obj1.factors();

    print("sum of factors");
    obj1.sumoffactors();



if __name__=="__main__":
    main();