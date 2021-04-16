
triedinput=" "
actualpass="Myname"
count=5
flag=0

while count>0:
    triedinput=input("Enter password: ")
    if(triedinput==actualpass):
        print("Congrats!! You have unlock the password ")
        flag=1
        break
    count = count-1
if( flag == 0):
    print("you have tried many times,please try again later")


