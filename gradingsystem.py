#grading system
import math

def course():
    I=True
    F=0
    Z=0
    Q=0
    U=0
    while I:
        x=[]
        counter=0
        classes=raw_input("Enter the class which you have: ")
        units=input("Enter the number of units it is: ")
        x.append(classes)
        g=True
        
        while g:
            u=input("Enter your mark: ")
            p=input("Enter the weighting of the mark: ")
            j=float(u)/100
            x.append(j)
            x.append(p)
            counter+=2
            c=raw_input("want to enter another mark? (yes or no): ")
            
            if c[0]=="y":
                g=True
            else:
                
                g=False
        
        X=0
        Y=0
        for i in range(0,counter-1,2):
            X+=x[i+1]*x[i+2]
        for i in range(0,counter-1,2):
            Y+=x[i+2]
        B=float(X)/Y*100

        if B>=90:
            V=12
        elif B>=85:
            V=11
        elif B>=80:
            V=10
        elif B>=77:
            V=9
        elif B>=73:
            V=8
        elif B>=70:
            V=7
        elif B>=67:
            V=6
        elif B>=63:
            V=5
        elif B>=60:
            V=4
        elif B>=57:
            V=3
        elif B>=53:
            V=2
        elif B>=50:
            V=1
        else:
            V=0
        Z+=float(X)/Y*100
        Q+=float(V)*units
        U+=units
        F+=1
        print "Your average for", classes, "is :" , B , "-->", V
        A=raw_input("want to enter another course? (yes or no): ")
        if A[0]=="y":
            I=True
        else:
            I=False 
  
    C=Z/F
    D=Q/U
    print "Your overall average for your life is ", C, "-->", D
    
course()

           
