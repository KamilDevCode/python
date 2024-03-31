# recursion:

# 

def countdown(num):
    print(num)
    if num == 0:
        return
    else:
        countdown(num - 1)

countdown(5)

def  countdown2(num):
    if num == 0:
        return
    else:
        print(num)
        countdown2(num - 1)

countdown2(5)

def add_num(num):
    if(num >= 9):
        return num + 1
    total = num + 1
    print(total)
    return add_num(total)

newtotal = add_num(6)
print(newtotal)