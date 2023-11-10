
def main():
    v = input("Greeting: ")
    print(f"{value(v)}")


def value(greeting):
    if "hello" in greeting.lower():
        return 0
    elif greeting.startswith("H") or greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()