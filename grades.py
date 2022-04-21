import string
import time

thresholds = [49, 59, 69, 74, 100]
class_names = {
    49: "Fail",
    59: "Third Class",
    69: "Second Class (Division 2)",
    74: "Second Class (Division 2)",
    100: "First Class",
}


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


def get_grade(grade: int):
    for thresh in thresholds:
        if grade >= thresh:
            continue
        else:
            return class_names[thresh]


if __name__ == "__main__":
    grade = take_input("📈 Enter your grade (%): ", int)
    class_name = get_grade(grade)
    if class_name == "Fail":
        print("you failed!")
        while True:
            print("😳", end="")
            time.sleep(0.5)
    else:
        print("You are in: ", class_name, "😻😻😻")
