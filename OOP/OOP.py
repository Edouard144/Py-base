class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old")

# create an object
person1 = Person(Edouard, 18)

# call the method
person1.introduce()




#codes of banking system
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


my_account = BankAccount(100)

my_account.deposit(50)
print(f"Balance after deposit: {my_account.balance}")

my_account.withdraw(30)
print(f"Balance after withdrawal: {my_account.balance}")

#returning string
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
        return "Success"
    return "Insufficient balance"


