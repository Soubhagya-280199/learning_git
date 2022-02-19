class practice:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
        #test case
        if self.a <= 0 and self.b <= 0:
            print("values are less than or equals to zero so answer is zero")
            exit()

    def addition(self):
        return self.a + self.b




obj = practice(0,0)
print( "sum of two values are ",obj.addition())
