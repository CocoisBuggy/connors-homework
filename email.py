import string
import re

EMREG = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
domain = "myuct.ac.za"


def validate_input(func):
    """
    Conform to RFC 5322 (https://www.rfc-editor.org/rfc/rfc5322)
    We are in control of structure.
    """

    def perf(**kwargs):
        user_input = func(**kwargs)
        check = set(string.ascii_letters + string.digits)
        for char in user_input:
            if char not in check:
                raise ValueError("Invalid user input. Try again")
        # Safe
        return user_input

    return perf


def validate_output(func):
    def v():
        output = func()  # perform target
        output = output.lower()  # adhere to lowercase internal convention

        if not re.fullmatch(EMREG, output):
            raise ValueError("Invalid email address generated. Please check your input")

        return output

    return v


@validate_input
def take_input(msg: str = ""):
    return input(msg)


@validate_output
def get_email():
    name = take_input(msg="Enter your name: ")
    last_name = take_input(msg="Enter your last name: ")
    return f"{name}_{last_name}@{domain}"


if __name__ == "__main__":
    email = get_email()
    print("📨📨📨 Your new email:", email)
    # place into db or whatever...
