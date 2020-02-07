
print("Enter two elements");

a=int(input());
b=int(input());

fp=lambda a,b: a*b;
ret=fp(a,b)

print("Multiplication of ",a,"&",b,"is",ret);

