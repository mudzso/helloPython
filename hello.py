import sys
arg = sys.argv
def sayHello():
    who = "World"
    if len(arg) > 1:
        who = arg[1]
    print("Hello " + who + "!")
sayHello()