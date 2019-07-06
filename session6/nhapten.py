while True:
    n= input("nhap vao ten cua ban:")
    print(n)
    if n.isdigit():
        print("that's not your name")
        print("please enter your name again:")
    else:
        print("ok")
        break


