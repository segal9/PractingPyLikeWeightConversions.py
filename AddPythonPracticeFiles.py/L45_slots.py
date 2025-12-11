# simple slot machine game to review:
import random

def spin_row():
    #pass
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    # use list comprehension
    '''
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
    '''
    # otherwise a list comp
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    #pass
    print("!!!!!!!!!!!!!!!!!")
    print(" | ".join(row))
    print("!!!!!!!!!!!!!!!!!")

def get_pay_out(row, bet):
    #pass
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0 
def main():
    balance = 100
    print("!!!!!!!!!!!!!!!!!")
    print("Sup at some Spinny Slots!")
    print("!!!!!!!!!!!!!!!!!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place an amount you want to bet: ")

        if not bet.isdigit():
            print("Enter a valid number")
            continue
        bet = int(bet) 

        if bet > balance:
            print("Insufficient funds!")
            continue
        
        if bet <= 0:
            print("bet must be great than 0!")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning!\n")
        print_row(row)

        payOut = get_pay_out(row, bet)

        if payOut > 0:
            print(f"You won $ {payOut}")
        else:
            print("Sorry you lost this round!")
        
        balance += payOut

        playAgain = input("Do you want to spin again? (Y/N): ").upper()

        if playAgain != "Y": 
            break
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")    
    print(f"Game over. Your final balance is ${balance}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")  
if __name__ == '__main__':
    main()