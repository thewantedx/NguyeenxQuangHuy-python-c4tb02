while True:
    from random import randrange
    n=randrange(30)
    m=randrange(30)
    i=randrange(2)
    x=randrange(2)
    if i==1:
        p=n-m
        print(n , "-" , m)
        s=randrange(100) 
        if x==0:
            print( s )
            trueorfalse=input("True or False")
            if trueorfalse== "True":
                print("you wrong")
                break
        else:
            print( p )
            trueorfalse=input("True or False")
            if trueorfalse== "False":
                print("you wrong")
                break   
    elif i==0:
        p=n+m
        print(n, "+", m)
        s=randrange(100)
        if x==0:
            print( s )
            trueorfalse=input("True or False")
            if trueorfalse== "True":
                print("you wrong")
                break
        else:
            print( p )
            trueorfalse=input("True or False")
            if trueorfalse== "False":
                print("you wrong")
                break 
       

 