def calculate(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
    return result


def main():
    print(calculate([int(input("Saisir un nombre")), int(input("Saisir un nombre")), int(input("Saisir un nombre"))]))


if __name__ == '__main__':
    main()
