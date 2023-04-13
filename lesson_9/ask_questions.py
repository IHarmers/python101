
def main():
    name = input("What is your name?: ")
    surname = input("What is your family name?: ")
    print("Hello, {} {}!".format(name, surname))
    food = input("What is your favorite food?")
    print(f"I like {food.lower()} too!")


if __name__ == "__main__":
    main()
