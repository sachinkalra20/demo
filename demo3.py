x=int(input("enter any year"))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
     print("yes leap year")
else:
 print("not leap year")