def GetName():
    go=True
    while go:
        name = input("What is your name?")
        if name == '':
            print("Please enter a valid name")
        else:
            go=False
    print(DoSomething(name))

def DoSomething(name):
    msg="{} has a nice smile".format(name)
    return msg

        
GetName()
