class Account:
    def __init__(self):
        self.value = 0
        self.withdraw_value_limit = 500
        self.withdraw_counter_limit = 3
        self.withdraw_counter = 0
        self.transactions = []

    def deposit(self, value):
        value = float(value)
        if value <= 0:
            print("Operation failed! Cannot deposit a negative amount")
            return self.value
        self.value += value
        self.transactions.append(f'Deposited: +R${value:.2f}; New balance: R${self.value:.2f}')
        print(f"Deposit successful! New balance: R${self.value:.2f}")
        return self.value
    
    def withdraw(self, value):
        value = float(value)
        if value > self.value:
            print("Operation failed! Insufficient funds")
            return
        elif value > self.withdraw_value_limit:
            print("Operation failed! Cannot withdraw more than 500 at a time")
            return
        elif self.withdraw_counter >= self.withdraw_counter_limit:
            print("Operation failed! Withdraw limit reached")
            return
        
        self.value -= value
        self.withdraw_counter += 1
        self.transactions.append(f'Withdrawn: -R${value:.2f}; New balance: R${self.value:.2f}')
        print(f"Withdrawal successful! New balance: R${self.value:.2f}")
        return self.value

    def extract(self):
        print("\n--- EXTRATO DA CONTA ---")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current balance: R${self.value:.2f}\n")


account = Account()

account.deposit(1000)
account.withdraw(200)
account.withdraw(600)
account.extract()