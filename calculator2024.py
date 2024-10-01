while 1:
    a=float(input("enter a 1st number: "))
    c=input("what you want to do ? +,-,X,/: ")
    b=float(input("enter a 2nd number: "))
    e=0
    if c=="+":
        print("Result =",a+b)
        e=a+b
    if c=="-":
        print("Result =",a-b )
        e=a-b
    if c=="X":
        print("Result =",a*b)
        e=a*b
    if c=="/":
        print("Result =",a/b)
        e=a/b
    q=int(input("do you want to continue with this result\n if yes pls press 1\n if you want to continue pls press 2\n if you want to quite pls press 3\n: "))
    if q==2:
        continue
    if q==3:
        break
    if q==1:

        while 1:
            x=e
            c=input("what you want to do ? +,-,*,/ ")
            b=float(input("enter a 2nd number: "))

            if c=="+":
                print("Result =",x+b)
                e=x+b
            if c=="-":
                print("Result =",x-b )
                e=x-b
            if c=="X":
                print("Result =",x*b)
                e=x*b
            if c=="/":
                print("Result =",x/b)
                e=x/b
            y=int(input(f"you want to continue with that result if yess press:1\nif no press:2\n:"))
            if y==2:
                break
            if y==1:
                continue
    w=int(input(f"want to continue:1\nnot:2\n:"))
    if w==2:
        break
    if w==1:
        continue



