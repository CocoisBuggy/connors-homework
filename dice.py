import random
import time


class UserInterrupt(Exception):
    def __init__(self):
        pass


def ease(t):
    x = (t - 1) * (t - 1) * (t - 1) * (1 - t) + 1
    return x


def roll():
    lim = 25
    for i in range(1, lim):
        time.sleep(ease(i / lim) / 6)
        yield random.randint(1, 6)
    return random.randint(1, 6)


def cycle_dice():
    user_validation = input("Press R to roll the dice: ")

    if user_validation.lower() != "r":
        raise UserInterrupt

    # init the stdout
    print("Roll: 0", end="")

    # iter through dice roll
    for r in roll():
        print(f"\b{r}", end="")

    print(" 🎉🎉🎉\n")
    return r


if __name__ == "__main__":
    while True:
        try:
            final = cycle_dice()
        except (KeyboardInterrupt, UserInterrupt):
            print("\nCome back when you need more rolls!🎉\n")
