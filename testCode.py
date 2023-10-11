

mySentence = "loves the color"

color_list = ['red','blue','green','blue','black','yellow','purple','orange']

def ColorFunction(name):
    lst = []
    for i in color_list:
        msg="{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def GetName():
    go=True
    while go:
        name=input("What is your name?")
        if name == '':
            print("Please provide your name")
        elif name=='Mike':
            print("You suck")
        else:
            go=False
    lst = ColorFunction(name)
    for i in lst:
        print(i)

GetName()
