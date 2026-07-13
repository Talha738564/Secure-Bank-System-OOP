class Account:
    total_accounts=0
    
    def __init__(self,owner_name,account_number,balance):
        self.owner_name=owner_name
        self.__account_number=account_number
        self.__balance=balance
        Account.total_accounts+=1
    @property
    def account_number(self):
        return self.__account_number        
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
        if amount>0:
            self.__balance+=amount
        else:
            print("[Please Enter a Valid Amount to Deposit]")
                        
    def withdrawal(self,amount):
        if amount>0 and  amount <=self.__balance:
            self.__balance-=amount
        else:
            print("[Please Enter a Valid Amount to Withdrawal]")
    def monthly_interest(self):
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
        self.interest_rate=0.02
        self.min_balance=500
    def monthly_interest(self):
        self.balance+=(self.balance*self.interest_rate/12)
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
    def monthly_interest(self):
        return 0
    def withdrawal(self, amount):
        if amount> 0 and self.balance-amount>=-self.over_draft:
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
    
class Bank:
    def __init__(self,name):
        self.name=name
        self.customers=[]
    def add_customer(self,customer):
        self.customers.append(customer)      
    def find_account(self,account_Number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number==account_Number:
                    print(account)
    def apply_interest(self):
         for customer in self.customers:
            for account in customer.accounts:
                account.monthly_interest()




# ============ SETUP ============
c1 = Customer("Ali", 1)
c2 = Customer("Sara", 2)
c3 = Customer("Ahmed", 3)
acc1 = SavingAccount("Ali", 101, 20000)
acc2 = CheckingAccount("Sara", 102, 5000)
acc3 = PremiumChecking("Ahmed", 103, 8000, 500, 0.05)
c1.open_account(acc1)
c2.open_account(acc2)
c3.open_account(acc3)
b1 = Bank("HBL")
b1.add_customer(c1)
b1.add_customer(c2)
b1.add_customer(c3)

# ============ TEST 1: __str__ ============
print("--- Account Details ---")
print(acc1)
print(acc2)
print(acc3)

# ============ TEST 2: Deposit ============
print("\n--- Deposit ---")
acc1.deposit(5000)
acc1.deposit(-500)
acc1.deposit(0)
print(acc1)

# ============ TEST 3: Withdrawal ============
print("\n--- Withdrawal ---")
acc1.withdrawal(1000)
acc1.withdrawal(30000)
print(acc1)

# ============ TEST 4: Overdraft ============
print("\n--- Overdraft ---")
acc2.withdrawal(5100)
acc2.withdrawal(500)
print(acc2)

# ============ TEST 5: Monthly Interest ============
print("\n--- Before Interest ---")
print(acc1)
print(acc2)
b1.apply_interest()
print("\n--- After Interest ---")
print(acc1)
print(acc2)

# ============ TEST 6: Cashback ============
print("\n--- Cashback ---")
print(f"Before cashback: {acc3}")
acc3.apply_cashback(1000)
print(f"After cashback: {acc3}")

# ============ TEST 7: find_account ============
print("\n--- Find Account ---")
b1.find_account(101)
b1.find_account(999)

# ============ TEST 8: total_wealth ============
print("\n--- Total Wealth ---")
print(c1.total_wealth())

# ============ TEST 9: __eq__ ============
print("\n--- Equality ---")
acc4 = SavingAccount("Someone", 101, 999)
print(acc1 == acc4)
print(acc1 == acc2)

# ============ TEST 10: __add__ ============
print("\n--- Combined Balance ---")
print(acc1 + acc2)

# ============ TEST 11: Sorting ============
print("\n--- Sorted Accounts ---")
all_accounts = [acc1, acc2, acc3]
all_accounts.sort()
for acc in all_accounts:
    print(acc)

# ============ TEST 12: from_string ============
print("\n--- from_string ---")
acc5 = Account.from_string("Usman,Savings,104,12000")
print(acc5)
acc6 = Account.from_string("Zara,Checking,105,3000")
print(acc6)

# ============ TEST 13: validate_account_number ============
print("\n--- Validate Account Number ---")
Account.validate_account_number("1234")
Account.validate_account_number("123456")
Account.validate_account_number("12")
Account.validate_account_number("1234567")

# ============ TEST 14: total_accounts ============
print("\n--- Total Accounts Created ---")
print(f"Total accounts created: {Account.total_accounts}")






















        



                   









        











