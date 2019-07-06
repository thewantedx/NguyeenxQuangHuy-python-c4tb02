while True:
    n=input("password:")
    if n.isalpha():
        print("please enter your password again")
    elif n.isdigit():
        print("please enter your password again")
    else:
        if len(n) < 8:
            print("please enter your password again")
        else:
            break