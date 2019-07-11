items = ["soccer", "tennis", "chess", "badminton"]
print(items)
while True:
    a="C"
    b="R"
    c="U"
    d="D"
    print("C , R , U , D")
    pick = input("Pick one letter above (capital letters):")
    if pick==a:
        m= input("what else do u like?")
        items.append(m)
        print(items)
    elif pick==b:
        m= len(items)
        if m==0: print("Nothing")
        else:
            for i in range(m):
                print(items[i])
    elif pick==c:
        while True:
            m= int(input("choose position u want to change(number?):"))
            if m>len(items): print("your number must >0 and <", len(items)+1)
            else: break
        p= input("What do you want to change it to:")
        items[m-1]= p
        print(items)
    else:
        while True:
            m= int(input("choose position u want to delete(number?):"))
            if m>len(items): print("your number must >0 and <", len(items)+1)
            else: break
        items.pop(m-1)
        print(items)
    

        