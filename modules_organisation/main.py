# from utils.sum import sum_numbers
# from utils.product import product_numbers

import utils as u


def play_with_calculator():
    print("Calculatrice : ")

    print("Somme de 2 nombres: ")
    input_user_for_sum = [int(input("Saisir le premier nombre ")), int(input("Saisir le second nombre "))]
    print("Résultat de la somme : ", input_user_for_sum[0], "+", input_user_for_sum[1], "=",
          u.sum_numbers(input_user_for_sum))

    print("Produit de 2 nombres: ")
    input_user_for_product = [int(input("Saisir le premier nombre ")), int(input("Saisir le second nombre "))]
    print("Résultat du produit : ", input_user_for_product[0], "*", input_user_for_product[1], "=",
          u.product_numbers(input_user_for_product))


def main():
    play_with_calculator()


if __name__ == '__main__':
    main()
