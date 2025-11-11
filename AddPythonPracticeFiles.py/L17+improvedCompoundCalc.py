# an improved compound interest calculator
def get_positive_float(question):
    while True:
        try:
            value = float(input(question))
            if value < 0:
                print("Value can't be negative. Try again!")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a numeric value.")

def compound_interest(principal, rate, time, frequency = 1):
    # using compound interest formulat: A = P * (1 + r/n)^(n*t)
    total = principal * pow((1 + rate / (100 * frequency )), frequency * time)
    interest = total - principal
    return total, interest

def main():
    print("---- Compound % Calculator ----")
    principal = get_positive_float("Enter the principal amount: $")
    rate = get_positive_float("Enter the annual interest rate (%): ")
    time = get_positive_float("Enter the time in years: ")

    # optional: Ask how often interest is compounded
    frequency = get_positive_float("Compound frequency per year (e.g. 1=yearly, 12=months): ")

    total, interest = compound_interest(principal, rate, time, frequency)

    print("\n--- Results ---")
    print(f"Principal: S{principal:,.2f}")
    print(f"Interest Earned: ${interest:,.2f}")
    print(f"Total Balance after {time} years: ${total:,.2f}")

if __name__ == "__main__":
    main()
