# simple banking program to practice py
# maybe about 60 lines of code
def show_balance(balance):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Your balance is ${balance:.2f}")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def deposit():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    amount =float(input("Enter an amount to be deposited: "))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if amount < 0:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Not a valid amount!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    else:
       return amount 

def withdraw(balance):
    #pass
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    amount = float(input("Enter an amount to withdraw: "))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if amount > balance:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Insufficient funds.")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    elif amount < 0:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Amount must be greater than 0!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return 0
    else:
        return amount

# for readibility encapsolate the main portion in main:
# to fix the sudden tab not working, hit: ctrl + M
def main():

    balance = 0
    is_running = True
    while is_running:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Banking game")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        choice = input("Enter choice made (1-4): ")
    
        if choice == '1':
           show_balance(balance)
        elif choice == '2':
           balance += deposit()
        elif choice == '3':
           balance -= withdraw(balance)
        elif choice == '4':
           is_running = False
        else:
           print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
           print("Invalid choice. Please pick (1-4)!")
           print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Thanks! Bye!")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
if __name__ == '__main__':
    main()