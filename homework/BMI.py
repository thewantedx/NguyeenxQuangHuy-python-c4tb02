n=int(input("nhap vao chieu cao(cm):"))
m=int(input("nhap vao can nang(kg):"))
bmi=m/((n/100)**2)
if bmi<16:
    print("you're severely underweight")
elif bmi<18.5:
    print("you're underweight")
elif bmi<25:
    print("you're normal")
elif bmi<30:
    print("you're overweight")  
else:
    print("you're obese")      