class User:
    def __init__(self, name, born_date, cpf, address):
        self.name = name
        self.born_date = born_date
        self.cpf = cpf
        self.address = address

    def __str__(self):
            return self.name

class Address:
    def __init__(self, street, number, neighborhood, city, state):
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood} - {self.city} / {self.state}"

class Account:
    def __init__(self, user=None):
        self.value = 0
        self.withdraw_value_limit = 500
        self.withdraw_counter_limit = 3
        self.withdraw_counter = 0
        self.transactions = []
        self.user = user

    def deposit(self, value, /):
        value = float(value)
        if value <= 0:
            print("Operation failed! Cannot deposit a negative amount")
            return self.value
        self.value += value
        self.transactions.append(f'Deposited: +R${value:.2f}; New balance: R${self.value:.2f}')
        print(f"Deposit successful! New balance: R${self.value:.2f}")
        return self.value
    
    def withdraw(*, self, value):
        value = float(value)
        if value > self.value:
            print("Operation failed! Insufficient funds")
            return False
        elif value > self.withdraw_value_limit:
            print("Operation failed! Cannot withdraw more than 500 at a time")
            return False
        elif self.withdraw_counter >= self.withdraw_counter_limit:
            print("Operation failed! Withdraw limit reached")
            return False
        
        self.value -= value
        self.withdraw_counter += 1
        self.transactions.append(f'Withdrawn: -R${value:.2f}; New balance: R${self.value:.2f}')
        print(f"Withdrawal successful! New balance: R${self.value:.2f}")
        return self.value

    def extract(self, /, *, show_balance=True):
        print("\n--- EXTRATO DA CONTA ---")
        for transaction in self.transactions:
            print(transaction)
        if show_balance:
            print(f"Saldo atual: R${self.value:.2f}\n")


def create_user(*, name, born_date, cpf, street, number, neighborhood, city, state):
    address = Address(street, number, neighborhood, city, state)
    user = User(name, born_date, cpf, address)
    return user

def create_account(user):
    if not isinstance(user, User):
        raise ValueError("Invalid user provided")
    account = Account(user)
    print(f"Account created successfully for {user.name}!")
    return account