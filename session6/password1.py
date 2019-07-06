while True:
    n= input("password:")
    if n.isdigit():
        print("please enter your password again:")
    elif n.isalpha():
        print("please enter your password again")
    else:
        break
