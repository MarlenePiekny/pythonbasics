def calculate(*numbers):
    sum_result = 0
    for number in numbers:
        sum_result += number
    return sum_result


def concatenate(**words):
    return " ".join(words.values())


def main():
    assert 10 == calculate(1, 2, 3, 4)

    assert "Hola! Como estas?" == concatenate(first="Hola!", second="Como", third="estas?")


if __name__ == '__main__':
    main()
