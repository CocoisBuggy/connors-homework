from numpy_financial import pmt
import string


def take_input(msg, dtype):
    while True:
        y = input(msg + " ")

        try:
            if dtype is float or dtype is int:
                y = "".join([p for p in y if p in string.digits + "."])
            z = dtype(y)
            return z
        except (TypeError, ValueError):
            print(f"Invalid input. Try again (needs to be {dtype})")


def compute_repayment():
    loan_amount = take_input("💸 Enter loan amount (R)", float)
    duration = take_input("📅 Enter duration (months)", int)
    interest_rate = take_input("📈 Enter interest rate (%)", float)

    # I have no idea, this is accountant shit
    repayment = pmt(interest_rate, duration, loan_amount)

    return repayment


if __name__ == "__main__":
    repayment = compute_repayment()
    print(f"Your Monthly Repayment is {repayment}")
