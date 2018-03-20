for t in range(int(input())):
    x=int(input())
    c=0;
    n=1
    i=1
    if(x==1):
        print(1)
    elif(x==2):
        print(2)
    elif(x==3):        
        print(2)
    else:    
        while(n<x):
            y=n;
            n = int(i*(i+1)/2)
            print(n)
            i+=1
            c+=1
        y = x-y
        n = n-x
        print(y)
        print(n)    
        if(y<n):
            print(c-1+y)
        else:
            print(c+n)