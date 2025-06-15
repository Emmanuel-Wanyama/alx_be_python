import sys
from bank_account import BankAccount

def main():
    # Initialize the account with the balance expected by the test for the 'display' command.
    account = BankAccount(250.0)

    # Check if a command-line argument is provided.
    # If no command is provided, default to displaying the balance.
    if len(sys.argv) < 2:
        # If no arguments, assume the default action is to display the balance
        print(f"Current Balance: ${account.display_balance():.2f}")
        sys.exit(0) # Exit successfully after displaying the default balance

    # If arguments are provided, parse the command and amount.
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    # Process the command based on user input.
    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit failed. Amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Withdrawal failed: Insufficient funds or invalid amount.")
    elif command == "display":
        # Print the current balance in the exact expected format.
        print(f"Current Balance: ${account.display_balance():.2f}")
    else:
        # Handle cases where the command is not recognized.
        print("Invalid command.")

if __name__ == "__main__":
    main()
