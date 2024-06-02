
#Python Programming internship at InternPe 
#Task 01: implementing simple calculator using python
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def pow(base,expo):
    return base**expo


while(1):
    
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.EXIT")
    op=int(input("choose one operation"))
    
    if op==1:
       n1=int(input("Enter first number"))
       n2=int(input("Enter second number"))
       print(n1,"+",n2,"=",add(n1,n2))
    elif op==2:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print(n1,"-",n2,"=",sub(n1,n2))
    elif op==3:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print(n1,"*",n2,"=",mul(n1,n2))
    elif op==4:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print(n1,"/",n2,"=",div(n1,n2))
    elif op==5:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print(n1,"^",n2,"=",pow(n1,n2))
    elif op==6:
        break
    else:
        print("Invalid Option")
         
print("EXITED")       
         
