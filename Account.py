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
        name,acc_type,account_number,balance=data.split(",")
        account_number=int(account_number)
        balance=float(balance)
        if acc_type=="Savings":
            return SavingAccount(name,account_number,balance)
        elif acc_type=="Checking":
            return CheckingAccount(name,account_number,balance)
        else:
            raise ValueError("Type of Account is Missing")

class SavingAccount(Account):

    def __init__(self,owner_name,account_number,balance):
        super().__init__(owner_name,account_number,balance)
        self.interst_rate=0.02
        self.min_balance=500
    def monthly_interst(self):
        self.balance+=(self.balance*self.interst_rate/12)
    def withdrawal(self,amount):
        if amount>0 and  self.balance-amount>=  self.min_balance :
            self.balance-=amount
        else:
            print(f"Balance is lower than minimum Balance {self.min_balance}  ")
                
        
class CheckingAccount(Account):
    def __init__(self,owner_name,account_number,balance,over_draft=200):
        super().__init__(owner_name,account_number,balance)
        self.over_draft=over_draft
        
    @property
    def balance(self):
        return super().balance
    @balance.setter
    def balance(self,value):
        if value >=-self.over_draft:
            self._Account__balance=value  
        else:
            print(" Invalid Value ")
    def monthly_interst(self):
        return 0
    def withdrawal(self, amount):
        if amount>= 0 and self.balance-amount>=-self.over_draft:
            self.balance-=amount
            if self.balance<0:
                print(f"You have the debt of the {-self.balance}$")
            
        else:
            print("You can't wtihdrawal that amount(OVER-DRAFT limit also crossed) ")  

class RewardMixin:
    def __init__(self,reward_rate):
        self.reward_rate=reward_rate
    cashback_rate=0.01
    def apply_cashback(self,purchase_amount):
        self.balance+=purchase_amount*self.cashback_rate
    def reward_calculation(self,amount):
        return amount*self.reward_rate        

class PremiumChecking(CheckingAccount,RewardMixin):
    def __init__(self,owner_name,account_number,balance,over_draft,reward_rate):
        CheckingAccount.__init__(self,owner_name,account_number,balance,over_draft)
        RewardMixin.__init__(self,reward_rate)

class Customer:
    total_accounts=0
    def __init__(self,name,customer_id):
        self.name=name
        self.customer_id=customer_id
        self.accounts=[]

    def open_account(self,account):
        self.accounts.append(account)
        Customer.total_accounts+=1
    def total_wealth(self):
        Total=0
        Total=sum(account.balance for account in self.accounts)
        return f"The Total Balance is: {Total}"

















        



                   









        











