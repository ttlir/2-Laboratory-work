Задание 1
class BankAccount:
    def _init_(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен на {amount} руб. Новый баланс: {self.balance} руб.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Средства в размере {amount} руб. сняты со счета. Новый баланс: {self.balance} руб.")
        else:
            print("Недостаточно средств на счете.")

    def _str_(self):
        return f"Имя владельца: {self.owner_name}\nНомер счета: {self.account_number}\nБаланс: {self.balance} руб."


# Пример использования класса BankAccount
account1 = BankAccount("Иванов Иван", "1234567890", 1000)
print(account1)

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)

Задание 2
class BankAccount:
    def _init_(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Счет пополнен на {amount} руб. Новый баланс: {self.balance} руб.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Средства в размере {amount} руб. сняты со счета. Новый баланс: {self.balance} руб.")
        else:
            print("Недостаточно средств на счете.")

    def _str_(self):
        return f"Имя владельца: {self.owner_name}\nНомер счета: {self.account_number}\nБаланс: {self.balance} руб."


# Пример использования класса BankAccount
account1 = BankAccount("Иванов Иван", "1234567890", 1000)
print(account1)

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)

Задание 3
class SavingAccount(BankAccount):
    def _init_(self, owner_name, account_number, balance=0, interest_rate=0):
        super()._init_(owner_name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Начислены проценты в размере {interest_amount:.2f} руб. Новый баланс: {self.balance:.2f} руб.")

# Пример использования класса SavingAccount
account2 = SavingAccount("Петров Петр", "0987654321", 2000, 5)
print(account2)

account2.add_interest()

Задание 4
class BankAccount:
    def _init_(self, owner_name, account_number, balance=0):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Ошибка: баланс не может быть отрицательным.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Счет пополнен на {amount} руб. Новый баланс: {self._balance} руб.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Средства в размере {amount} руб. сняты со счета. Новый баланс: {self._balance} руб.")
        else:
            print("Недостаточно средств на счете.")

    def _str_(self):
        return f"Имя владельца: {self._owner_name}\nНомер счета: {self._account_number}\nБаланс: {self._balance} руб."


# Пример использования класса BankAccount
account = BankAccount("Иванов Иван", "1234567890", 1000)
print(account)

# Использование геттеров и сеттеров
account.set_balance(2000)
print("Новый баланс:", account.get_balance())

# Попытка установить отрицательный баланс
account.set_balance(-500)

Задание 5
class BankAccount:
    def _init_(self, owner_name, account_number, balance=0):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Ошибка: баланс не может быть отрицательным.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Счет пополнен на {amount} руб. Новый баланс: {self._balance} руб.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Средства в размере {amount} руб. сняты со счета. Новый баланс: {self._balance} руб.")
        else:
            print("Недостаточно средств на счете.")

    def _str_(self):
        return f"Имя владельца: {self._owner_name}\nНомер счета: {self._account_number}\nБаланс: {self._balance} руб."

    def _eq_(self, other):
        return self._balance == other.get_balance()

    def _lt_(self, other):
        return self._balance < other.get_balance()

    def _gt_(self, other):
        return self._balance > other.get_balance()


# Пример использования специальных методов
account1 = BankAccount("Иванов Иван", "1234567890", 1000)
account2 = BankAccount("Петров Петр", "0987654321", 2000)

print("Сравнение по балансу:")
print("account1 == account2:", account1 == account2)
print("account1 < account2:", account1 < account2)
print("account1 > account2:", account1 > account2)

account3 = BankAccount("Сидоров Сидор", "1357924680", 1500)
account4 = BankAccount("Федоров Федор", "0246813579", 1500)

print("\nСравнение по балансу:")
print("account3 == account4:", account3 == account4)
print("account3 < account4:", account3 < account4)
print("account3 > account4:", account3 > account4)