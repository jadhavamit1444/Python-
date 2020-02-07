
class arithmetic:

    def __init__(self):
        self.value1=0;
        self.value2=0;

    def accept(self,no1,no2):
        self.value1=no1;
        self.value2=no2;

    def addition(self):
        print("Addition =",(self.value1+self.value2));

    def subtraction(self):
        print("Subtraction =",(self.value1-self.value2));

    def multiplication(self):
        print("Multiplication =",(self.value1*self.value2));

    def division(self):
        print("Division =",(self.value1/self.value2));

def main():
    obj1=arithmetic();
    obj1.accept(int(input("Enter first value")), int(input("Enter second value")));
    obj1.addition();
    obj1.subtraction();
    obj1.multiplication();
    obj1.division();
    
if __name__=="__main__" :
    main();
