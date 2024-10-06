import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = None

    if len(command_parts) == 2:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Available commands: deposit, withdraw, display.")

if __name__ == "__main__":
    main()
