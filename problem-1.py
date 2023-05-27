class GoCardAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = [("Initial balance", initial_balance)]

    def record_ride(self, amount):
        self.balance -= amount
        self.transactions.append(("Ride", amount, self.balance))

    def record_top_up(self, amount):
        self.balance += amount
        self.transactions.append(("Top up", amount, self.balance))

    def get_balance(self):
        return self.balance

    def generate_statement(self):
        statement = "Statement:\n"
        statement += "{:<20}{:<12}{:<12}\n".format("event", "amount ($)", "balance ($)")
        for transaction in self.transactions:
            event, amount, balance = transaction
            statement += "{:<20}{:<12.2f}{:<12.2f}\n".format(event, amount, balance)
        return statement


def process_command(command, account, bad_commands):
    parts = command.split()
    if len(parts) == 0:
        return

    action = parts[0]
    if action == "q":
        return False
    elif action == "b":
        print(f"Balance = ${account.get_balance():.2f}")
    elif action == "r" and len(parts) == 2 and parts[1][0].isdigit():
        amount_str = parts[1]
        try:
            amount = float(amount_str)
            account.record_ride(amount)
        except ValueError:
            if len(bad_commands) < 3:
                bad_commands.append(command)
    elif action == "t" and len(parts) == 2 and parts[1][0].isdigit():
        amount_str = parts[1]
        try:
            amount = float(amount_str)
            account.record_top_up(amount)
        except ValueError:
            if len(bad_commands) < 3:
                bad_commands.append(command)
    else:
        if len(bad_commands) < 3:
            bad_commands.append(command)

    return True


initial_balance = float(input("Creating account. Input initial balance: "))
account = GoCardAccount(initial_balance)
bad_commands = []

command = input("? ")
while process_command(command, account, bad_commands):
    command = input("? ")

final_balance = account.get_balance()

print("Statement:")
print("event            amount ($)  balance ($)")
print("Initial balance              {:.2f}".format(initial_balance))
for transaction in account.transactions[1:]:
    event, amount, balance = transaction
    print("{:<20}{:<12.2f}{:<12.2f}".format(event, amount, balance))

print("Final balance\t\t\t{:.2f}".format(final_balance))
