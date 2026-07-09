class Account:
    total_accounts=0
    
    def __init__(self,owner_name,account_number,balance):
        self.owner_name=owner_name
        self.__account_number=account_number
        self.__balance=balance
        Account.total_accounts+=1
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value >=0:
            self.__balance=value  
        else:
            print("Negative Balance is not Valid")
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
        else:
            print("[Please Enter a Valid Amount to Deposit]")
                        
    def withdrawal(self,amount):
        if amount>0 and  amount <=self.__balance:
            self.__balance-=amount
        else:
            print("[Please Enter a Valid Amount to Withdrawal]")
    def monthly_interst(self):
        pass
    def __str__(self):
        return (f"Account#{self.__account_number} ({self.owner_name}) - Balance: ${self.__balance}")
    def __eq__(self,other):
        return self.__account_number==other.__account_number
    def __lt__(self,other):
        return self.__balance<other.balance
    def __add__(self, other):
        Total=self.__balance+other.balance
        return f"The Total of these two accounts  is: {Total}"
    @staticmethod
    def validate_account_number(number):
        if len(number)>= 4 and  len(number)<= 6:
            print("[Valid Account Number]")
        else:
            print("[Invalid Account Number]")
    @classmethod
    def from_string(cls,data):
        name,acc_type,balance=data.split(",")
        balance=float(balance)
        account_number=cls.total_accounts+1  
        if acc_type=="Savings":
            return SavingAccount(name,account_number,balance)
        elif acc_type=="Checking":
            return CheckingAccount(name,account_number,balance)

class SavingAccount(Account):
    pass
class CheckingAccount(Account):
    pass            


        



                   










        











