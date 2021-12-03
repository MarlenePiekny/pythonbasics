# This script aims to calculate the sales amount of company sales representative


sales = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}


def sum_sales():
    total = 0
    for sales_from_representative in sales.values():
        total += sales_from_representative
    return total


def get_representative_name_from_sales(value: int):
    for name, sale in sales.items():
        if sale == value:
            return name
    return -1


def best_sale_representative():
    return get_representative_name_from_sales(max(sales.values()))


def main():
    print(sum_sales())
    print(best_sale_representative())


if __name__ == '__main__':
    main()
