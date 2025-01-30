class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
        self.bal-=amount
        print("Rs",amount,"was debited")
        print("Total balance is",self.getbal())
    
    def credit(self,amount):
        self.bal+=amount
        print("Rs",amount,"was credited")
        print("Total balance is",self.getbal())

    def getbal(self):
        return self.bal
acc1=Account(10000,1234)
print(acc1.bal)
print(acc1.acc)

acc1.debit(1000)
acc1.credit(5000)