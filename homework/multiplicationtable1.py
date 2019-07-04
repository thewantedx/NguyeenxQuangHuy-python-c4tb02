for row in range(1, 10):
    for col in range(1, 10):
        num = row * col
        if num < 10: blank = '  '       
        else:
            if num < 100: blank  = ' '  
        print(blank, num, end = '')     
    print()                      