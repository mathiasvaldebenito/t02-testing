class Arithmetic:


    def sum_a(self):
        a = 3
        b = 1
        a = a + 1 # ejemplo 1
        a = 1 + a # ejemplo 2
        a = a + b # ejemplo 3
        b = b + b # ejemplo 3
        b = a + 2
        b = b + 32
        a += 23
    
    def ifs(self):
        if 2 + 2 == 3:
            print("what?")
            print("nonsense")
            print("again, what?")
        elif 2*2 == 3:
            print("haha")
        else:                   #ejemplo 1
            pass
        if 2 + 2 == 4:
            print("thank god")
            print("finally some logic")
            if 2 + 2 == 23:
                print("jm")
                if "ja" == "ha":
                    print("haja")
                else:
                    pass
            else:               # ejemplo 2
                pass
        else:
            if "lets" == "see":
                a = 3
                b = 2
                a = a + 23
                b = b + a
            else:
                pass

    def if_and_else(self):
        if 2 + 2 == 3:
            print("what?")
            print("nonsense")
            print("again, what?")
        if 2 + 2 == 5:
            print("and again")
            print("what's wrong with you?")
        else:
            print("IN ELSE")
