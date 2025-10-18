class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder 
        self.balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount            
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")  

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")

            if amount > self.balance:
                raise Exception("Insufficient funds!")  
            self.balance -= amount        
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        except Exception as e:
            print(f"Error: {e}")    

    def get_balance(self):
        return self.balance
    
    def get_account_holder(self):
        return self.account_holder
    
        
