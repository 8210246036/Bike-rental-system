class bikeshope:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("total bikes", self.stock)
    def rentforbike(self,q):

        if q<=0:
            print("enter the postive value or greater than zero")
        elif q>self.stock:
            print("enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("total price",q*100)
            print("total bikes", self.stock)

while True:
    obj=bikeshope(100)
    uc=int(input('''
1 Display stocks
2 Rent a bike 
3 Exit 
    '''))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("enter the Qty..."))
        obj.rentforbike(n)
    else:
        break


