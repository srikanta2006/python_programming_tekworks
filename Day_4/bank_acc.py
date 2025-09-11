class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        self.__balance+=amount
        print("Money deposited")
    
    def withdraw(self, amount):
        if(amount<=self.__balance):
            self.__balance-=amount
            print("Money withdrawed")
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        print(f"Your account balance is: {self.__balance}")

b1=BankAccount()
b1.deposit(5000)
b1.withdraw(2000)
b1.get_balance()
