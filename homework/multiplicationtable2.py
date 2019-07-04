n=int(input("nhap vao 1 so:"))
for row in range(1, n+1):
    for col in range(1, n+1):
        num = row * col
        if num < n: blank = '  '       
        else:
            if num < n**2: blank  = ' '  
        print(blank, num, end = '')     
    print()                              