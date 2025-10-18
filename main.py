from bank_account import BankAccount

account = BankAccount("Norah", 515)

print("Account Holder:", account.get_account_holder())
print("Current Balance:", account.get_balance())

print(account.deposit(222)) 
print(account.withdraw(777))
print(account.withdraw(2000))

print("Fainal Balance:", account.get_balance())