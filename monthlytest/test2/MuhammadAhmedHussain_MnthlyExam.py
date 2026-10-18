SUMMARY_FILENAME = 'loan_summary.txt'


def read_number(prompt, error_message, is_valid, as_integer=False):
    while True:
        raw_text = input(prompt).strip().replace(',', '')
        try:
            value = int(raw_text) if as_integer else float(raw_text)
        except ValueError:
            print(f'  Error: {error_message} (non-numeric input).')
            continue

        if isinstance(value, float) and value - value != 0:
            print(f'  Error: {error_message}.')
            continue

        if is_valid(value):
            return value
        print(f'  Error: {error_message}.')


def get_validated_input():
    principal = read_number(
        'enter principal amount:',
        'number must be greater than 0',
        lambda value: value > 0,
    )
    annual_rate = read_number(
        'enter annual interest rate:',
        'number must be greater than 0 or equal to 0',
        lambda value: value >= 0
    )
    tenure_months = read_number(
        'enter loan tenure (months):',
        'number must be a positive whole number',
        lambda value: value > 0,
        as_integer=True
    )
    return principal, annual_rate, tenure_months


def calculate_emi(principal, rate, tenure):
    if rate == 0:
        return round(principal / tenure, 2)
    monthly_rate = rate / 12/100
    growth_factor = (1 + monthly_rate) ** tenure
    emi = principal * monthly_rate * growth_factor / (growth_factor - 1)
    return round(emi, 2)


def calculate_totals(emi, principal, tenure):
    total_repayment = round(emi * tenure, 2)
    total_interest = round(total_repayment - principal, 2)
    return total_repayment, total_interest


def generate_repayment_schedule(principal, rate, tenure, emi):
    monthly_rate = rate / 12 / 100
    schedule = []
    opening_balance = round(principal, 2)

    for month in range(1, tenure + 1):
        interest = round(opening_balance * monthly_rate, 2)
        principal_paid = round(emi - interest, 2)
        payment = emi

        if month == tenure or principal_paid > opening_balance:
            principal_paid = opening_balance
            payment = round(principal_paid + interest, 2)

        closing_balance = round(opening_balance - principal_paid, 2)
        if closing_balance < 0:
            closing_balance = 0.0

        schedule.append({
            'month': month,
            'opening': opening_balance,
            'interest': interest,
            'principal_paid': principal_paid,
            'payment': payment,
            'closing': closing_balance,
        })
        opening_balance = closing_balance

    return schedule


def display_repayment_schedule(schedule):
    header = (f"{'Month':>5} {'Opening':>14} {'Interest':>12} "
              f"{'Principal':>14} {'Payment':>12} {'Closing':>14}")
    print("\n" + header)
    print("-" * len(header))
    for row in schedule:
        print(f"{row['month']:>5} {row['opening']:>14,.2f} "
              f"{row['interest']:>12,.2f} {row['principal_paid']:>14,.2f} "
              f"{row['payment']:>12,.2f} {row['closing']:>14,.2f}")
    print("-" * len(header))


def save_summary_to_file(principal, rate, tenure, emi,
                         total_repayment, total_interest,
                         filename=SUMMARY_FILENAME):
    try:
        with open(filename, "w") as summary_file:
            summary_file.write("LOAN SUMMARY\n")
            summary_file.write("=" * 32 + "\n")
            summary_file.write(f"Principal         : {principal:,.2f}\n")
            summary_file.write(f"Annual Rate (%)   : {rate:.2f}\n")
            summary_file.write(f"Tenure (months)   : {tenure}\n")
            summary_file.write(f"Monthly EMI       : {emi:,.2f}\n")
            summary_file.write(f"Total Repayment   : {total_repayment:,.2f}\n")
            summary_file.write(f"Total Interest    : {total_interest:,.2f}\n")
        return True
    except OSError as error:
        print(f"  Error: could not write '{filename}': {error}")
        return False


def print_menu():
    print("\n===== LOAN & EMI CALCULATOR =====")
    print("1. Calculate Loan EMI")
    print("2. Display Repayment Schedule")
    print("3. Save Summary to File")
    print("4. Exit")


def handle_calculate():
    principal, rate, tenure = get_validated_input()
    emi = calculate_emi(principal, rate, tenure)
    total_repayment, total_interest = calculate_totals(emi, principal, tenure)
    print("\n--- Loan Results ---")
    print(f"Monthly EMI     : {emi:,.2f}")
    print(f"Total Repayment : {total_repayment:,.2f}")
    print(f"Total Interest  : {total_interest:,.2f}")

    return {
        'principal': principal,
        'rate': rate,
        'tenure': tenure,
        'emi': emi,
        'total_repayment': total_repayment,
        'total_interest': total_interest
    }


def main():
    loan = None
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            loan = handle_calculate()

        elif choice == '2':
            if loan is None:
                print('Please calculate the loan first.')
            else:
                schedule = generate_repayment_schedule(
                    loan['principal'], loan['rate'], loan['tenure'], loan['emi'])
                display_repayment_schedule(schedule)

        elif choice == '3':
            if loan is None:
                print('Please calculate the loan first.')
            else:
                success = save_summary_to_file(
                    loan['principal'], loan['rate'], loan['tenure'],
                    loan['emi'], loan['total_repayment'], loan['total_interest'])
                if success:
                    print(f"Summary saved to '{SUMMARY_FILENAME}'.")

        elif choice == '4':
            print('Exiting the program.')
            break
        else:
            print("  Invalid option. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
