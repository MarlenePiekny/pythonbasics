# This script calculate item price including all taxes in euros

import math


class Item:
    def __init__(self, name, including_all_taxes_price, tax_price, stock=1, discount=0.0):
        self.name = name
        self.including_all_taxes_price = including_all_taxes_price
        self.tax_price = tax_price
        self.stock = stock
        self.discount = discount


ITEM_STOCK_VALUE = 1000  # threshold stock value in euros to get a 12% discount
DISCOUNT_RATE = 0.12


def round_rate_to_upper(vat_rate: float) -> float:
    return (math.ceil(vat_rate * 100)) / 100


# def price_including_all_taxes(item_price: float, item_vat_rate: float) -> float:
#     """Calculate price including all taxes given an item excluding price and its VAT
#         :rtype: float
#         :param item_price: item excluding price
#         :param item_vat_rate: item VAT in percentage
#         :return item price including all taxes
#
#     """
#     return float(item_price * (1 + item_vat_rate))
#
#
# def tax_price(item_price: float, item_vat: float) -> float:
#     """Calculate item tax price given an item excluding price and its VAT
#         :rtype: float
#         :param item_price: item excluding price
#         :param item_vat: item VAT in percentage
#         :return item tax price
#
#     """
#     return float(item_price * item_vat)


def get_item_data(item_name: str, item_price: float, item_vat_rate: float) -> Item:
    including_all_taxes_item_price = float(item_price * (1 + round_rate_to_upper(item_vat_rate)))
    tax_item_price = float(item_price * round_rate_to_upper(item_vat_rate))
    item_data = Item(item_name, including_all_taxes_item_price, tax_item_price)
    return item_data


def get_item_data_according_to_stock(item_name, item_price: float, item_vat_rate: float, item_stock: int) -> Item:
    if item_stock < 0:
        including_all_taxes_item_price = float(item_price * (1 + round_rate_to_upper(item_vat_rate))) * item_stock
        tax_item_price = float(item_price * round_rate_to_upper(item_vat_rate)) * item_stock
        return Item(item_name, including_all_taxes_item_price, tax_item_price, 0)

    elif item_stock < ITEM_STOCK_VALUE:
        including_all_taxes_item_price = float(item_price * (1 + round_rate_to_upper(item_vat_rate))) * item_stock
        tax_item_price = float(item_price * round_rate_to_upper(item_vat_rate)) * item_stock
        return Item(item_name, including_all_taxes_item_price, tax_item_price)

    elif item_stock >= ITEM_STOCK_VALUE:
        including_all_taxes_item_price = float(item_price * (1 + round_rate_to_upper(item_vat_rate))) \
                                         * (1 - DISCOUNT_RATE) * item_stock
        tax_item_price = float(item_price * round_rate_to_upper(item_vat_rate)) * item_stock
        item_discount = float(item_price * (1 + round_rate_to_upper(item_vat_rate)) * DISCOUNT_RATE * item_stock)
        return Item(item_name, including_all_taxes_item_price, tax_item_price, item_stock, item_discount)


def user_interaction_for_one_item():
    # item_name = "switch"
    # item_price_excluding_v_a_t = 100.0
    # item_vat = float(19.6)

    item_name = input("Quel est le nom du produit ?")
    item_price_excluding_v_a_t = float(input("Quel est le prix du produit en euros?"))
    item_vat_rate = float(input("Quel est le taux de TVA du produit ?"))

    # item_price_including_v_a_t = price_including_all_taxes(item_price_excluding_v_a_t, item_vat)
    # item_tax_price = tax_price(item_price_excluding_v_a_t, item_vat)

    item_data = get_item_data(item_name, item_price_excluding_v_a_t, item_vat_rate)

    # print(item_price_including_v_a_t, item_tax_price)

    # print("Le prix TTC du produit", item_name, "est de",
    #       item_price_including_v_a_t,
    #       "€ (taxes de", item_tax_price, "€)")
    #
    # print("Le prix TTC du produit", item_name, "est de",
    #       item_price_including_v_a_t,
    #       "€ (taxes de", float(item_price_including_v_a_t) - float(item_price_excluding_v_a_t), "€)")

    print("Le prix TTC du produit", item_data.name, "est de",
          item_data.including_all_taxes_price,
          "€ (taxes de", item_data.tax_price, "€)")


def user_interaction_for_item_stock():
    item_name = input("Quel est le nom du produit ?")
    item_price_excluding_v_a_t = float(input("Quel est le prix du produit en euros?"))
    item_vat_rate = float(input("Quel est le taux de TVA du produit ?"))
    item_stock = int(input("Quelle est la quantité d'article en stock ?"))

    items_data = get_item_data_according_to_stock(item_name, item_price_excluding_v_a_t, item_vat_rate, item_stock)

    print("Le total TTC du stock de", items_data.name, "est de ", items_data.including_all_taxes_price,
          "(dont taxes de", items_data.tax_price, "€")

    if item_stock >= ITEM_STOCK_VALUE:
        print("- remise de",  items_data.discount, "€)")
    else:
        print(")")


def main():

    user_interaction_for_item_stock()
    # user_interaction_for_one_item()


main()
