
class bankaccount:
    ROI=10.5;

    def __init__(self, name, amount):
        self.name=name;
        self.amount=amount;

    def deposit(self,dep):
        self.depos=self.amount+dep;

    def withdraw(self, wit):
        self.withd=self.depos-wit;

    def calculateinterest(self):
        self.intrest=(self.ROI/100)*self.withd;

    def display(self):
        print("Name of account holder", self.name);
        print("Amount= ", self.amount);
        print("Amount after deposit", self.depos);
        print("Amount after withdraw", self.withd);
        print("Total interest", self.intrest);

def main():
    obj1=bankaccount('AMIT', 5000);
    obj1.deposit(2000);
    obj1.withdraw(3500);
    obj1.calculateinterest();
    obj1.display();

if __name__=="__main__":
    main();