import time
c=0
m=0
p=0
def countdawon(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
def darug_stor():
    if order == "cosmotics":
        global c
        c += 1
        print(f"C - {c}")
    if order == "perfume":
        global p
        p += 1
        print(f"P - {p}")
    if order == "medicine":
        global m
        m += 1
        print(f'M - {m}')
def message(msg):
    return msg
msg1 = message("your number is")
msg2 = message("Please wait and someone will assist you shortly.")
Type_of_product = """ list of products:
1. perfume
2. cosmotics
3. medicine"""
print(" ******************Welcom to our  drug store**************************")
toda_list = [123456,14789]
count = 0
count_limit = 3
while count_limit > count:
    Toda = int(input("please enter your id: "))
    if Toda in toda_list:
        print(Type_of_product)
        order = input("please choose your product area from Type_of_product: ")
        while order != "":
            print(msg1)
            darug_stor()
            print(msg2)
            permission = input("do you want continue? y/n")
            if permission == "y" or permission == "Y":
                order = input("please choose your product area from list: ")
            else:
                exit(0)
        else:
            order = input( "please choose your product area from Type_of_product\nyour choese is out of Type_of_product:")
    else:
        print("please try again")
    count += 1
else:
    times = int(input("enter your time: "))
    for sec in range(0,times):
        time.sleep(1)
        print(f"00:00:0{sec}")




