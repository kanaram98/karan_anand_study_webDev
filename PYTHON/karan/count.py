a=int(input("enter number "))
operation=input("what you want to do - squre or count")

type(operation)

def count(a):
    i=1
    while(i<=a):
        print(i)
        i+=1
1
def squre(a):
    print(a**2)


def calculate(a,operation):
    if(operation=='squre'):
        squre(a)
    elif(operation=='count'):
        count(a)
        
    

calculate(a,operation)