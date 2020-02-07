

class circle:

    PI=3.14;

    def __init__(self):
        self.radius=0;
        self.area=0;
        self.circumference=0;

    def accept(self,no1):
        self.radius=no1;

    def calculatearea(self):
        self.area=self.PI*self.radius*self.radius;

    def calculatecircumference(self):
        self.circumference=float(self.PI*self.radius*2);


    def display(self):
        print("Radius", self.radius);
        print("Area of Circle", self.area);
        print("Circumference of circle", self.circumference);


def main():
    print("For object 1");
    obj1=circle();
    obj1.accept(int(input("value of radius=")));
    obj1.calculatearea();
    obj1.calculatecircumference();
    obj1.display();

    print("For object 2");
    obj2=circle();
    obj2.accept(int(input("value of radius=")));
    obj2.calculatearea();
    obj2.calculatecircumference();
    obj2.display();

    print("For object 3");
    obj2 = circle();
    obj2.accept(int(input("value of radius=")));
    obj2.calculatearea();
    obj2.calculatecircumference();
    obj2.display();

if __name__=="__main__":
    main();