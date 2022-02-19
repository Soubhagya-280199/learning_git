class difference:
    def minus(self,a,b):
        if a < b:
            temp = a
            a = b
            b = temp
        print(a-b)



obj = difference()
obj.minus(3,5)