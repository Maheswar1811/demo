import database as db

while(True):
    print("1.login")
    print("2.sign up")
    print("3.exit")
    print()
    choice=int(input("enter your choice: "))
    if choice==1:
        res=db.times()
        print(res)
        # for row in res:
        #     print(row)
    elif choice==2:
        name=input("enter your name: ")
        age=int(input("eneter your age: "))
        db.add_user(name,age)
    elif choice==3:
        break
