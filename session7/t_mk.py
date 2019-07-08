while True:
    n= input("tài khoản:")
    m= input("mật khẩu:")
    if len(m)<8: 
        print("nhập lại mật khẩu")
    elif m.isdigit():
        print("nhập lại mật khẩu")
    elif m.isalpha():
        print("nhập lại mật khẩu")
    else:
        p=input("xác nhận lại mật khẩu:")
        if p!=m:
            print("mật khẩu sai")
        else:
            while True:
                email= input("nhập email của bạn: ")
                if len(email)<8:
                    print("nhập lại email")
                elif email.isdigit():
                    print("nhập lại email")
                elif email.isalpha():
                    print("nhập lại email")
                elif "@" not in email:
                    print("nhập lại email")
                elif "." not in email:
                    print("nhập lại email")
                else:
                    break
        break            


