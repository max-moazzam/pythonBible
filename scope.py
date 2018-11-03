a = 100

def f1():
    global a
    a = 50
    print(a)

def f2():
    a = 150
    print(a)

f1()
f2()
print(a)
