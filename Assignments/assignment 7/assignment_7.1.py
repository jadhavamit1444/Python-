
class bookstore:

    Noofbooks=0;

    def __init__(self, no1, no2):
        self.name=no1
        self.author=no2;
        bookstore.Noofbooks+=1;

    def display(self):
        print(self.name);
        print(self.author);
        print(self.Noofbooks);

def main():
    obj1=bookstore('linux system programming by', 'robert love');
    obj1.display();

    obj2=bookstore('c programming by', 'denis ritchie');
    obj2.display();

if __name__=="__main__":
    main();