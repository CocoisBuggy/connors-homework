def is_odd(num):
    return num % 2 == 1


if __name__ == "__main__":
    try:
        while True:
            test = input("💯 Enter a number: ")
            try:
                encoded = int(test, 10)
            except ValueError:
                try:
                    print("⛔ base 10 failure... trying hex")
                    encoded = int(test, 16)
                except ValueError:
                    print(
                        "⛔ hex failure... accepting byte data (big-endian): ",
                        [hex(x) for x in bytes(test, "utf-8")],
                    )
                    encoded = int.from_bytes(bytes(test, "utf-8"), "big")

            print(f"{encoded} is\t", "odd 🐞" if is_odd(encoded) else "even 🐢")
    except KeyboardInterrupt:
        exit()
