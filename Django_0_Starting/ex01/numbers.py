def read_print():
    with open("numbers.txt", "r") as file:
        content = file.read()

    numbers = content.split(",")
    print(numbers)

    for number in numbers:
        print(number)

if __name__ == '__main__':
    read_print()