# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
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


