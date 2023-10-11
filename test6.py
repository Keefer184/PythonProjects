
def GetInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1, var2

def Compute():
    go=True
    while go:
        var1, var2 = GetInfo()
        try:
            var3 = int(var1) + int(var2)
            
            go = False
        except ValueError as y:
            print("{}: \n\nYou did not provide a numeric value!".format(y))
        except:
            print("\n\nYou broke it, program will now self-destruct....")
    print("{}+{}={}".format(var1, var2, var3))
    
    
     


if (__name__)=="__main__":
    Compute()
