# This script aims to manipulate data structures such as lists and stuples

from random import randint


L = [1, 4, "bonjour", 'T', 'M', 1]
L1 = [13, 15, 12, 17, 15]
L2 = ["Fifi", "Riri", "Loulou"]

L3 = [13, 15, 12, 17, 15]
L4 = [18, 15, 14, 13, 19, 20]

val = [12.5, 13.6, 18.4, 9.7]
coef = [2, 3, 5, 4]


def add_element_to_l3(element):
    L3.append(element)


def remove_element_from_l3_by_index(index):
    del L3[index]


def display_element_of_a_list_according_to_index(one_list: list, i: int):
    return one_list[i]


def insert_element_in_l3(element, index):
    L3.insert(index, element)


def display_index_of_an_element_in_a_list(one_list: list, element):
    return one_list.index(element)


def find_second_index_of_an_element_in_a_list(one_list: list, element):
    for first_element in one_list:
        if first_element == element:
            for i in range(one_list.index(element)+1, len(one_list)):
                if one_list[i] == element:
                    return i
            return -1
    return -1


def display_second_index_of_an_element_in_a_list(one_list: list, element):
    index = find_second_index_of_an_element_in_a_list(one_list, element)
    if index == -1 :
        print(index)
    else:
        print("Le deuxième", element, "se trouve à l'index", index)


def display_list(one_list):
    for element in one_list:
        print(element)


def chose_random_int() -> int:
    return randint(0, 100)


def generate_ascending_list_quantity_of_random_number(quantity: int):
    random_number_list = [chose_random_int() for i in range(quantity)]
    random_number_list.sort()
    return random_number_list


def ascending_sort_list(one_list: list):
    return one_list.sort()


def alternatively_concatenate_two_lists(first_list: list, second_list: list):
    concatenate_list = []
    concatenate_list_length = max(len(first_list), len(second_list))
    for i in range(0, concatenate_list_length-1):
        if i < len(first_list):
            concatenate_list.append(first_list[i])
        if i < len(second_list):
            concatenate_list.append(second_list[i])
    return concatenate_list


def concatenate_two_lists_without_duplication(first_list: list, second_list: list):
    new_list = first_list
    [new_list.append(second_list_element) for second_list_element in second_list
     if (second_list_element not in new_list)]
    return new_list


def calculate_weighted_average(value_list, coefficient_list):
    numerator = 0
    denominator = 0
    if len(value_list) != len(coefficient_list):
        return 0
    for i in range(len(value_list)):
        numerator += value_list[i] * coefficient_list[i]
        denominator += coefficient_list[i]
    return numerator // denominator





def main():
    # print("Afficher l'élément de la liste L d'indice 0 :",
    #       display_element_of_a_list_according_to_index(L, 0))
    # print("Afficher l'index de l'élement \"bonjour\" de la liste L :",
    #       display_index_of_an_element_in_a_list(L, "bonjour"))
    # display_second_index_of_an_element_in_a_list(L, 1)
    # display_list(generate_ascending_list_quantity_of_random_number(1000))
    # print(alternatively_concatenate_two_lists(L1, L2))
    # print(concatenate_two_lists_without_duplication(L3, L4))
    # print(calculate_weighted_average(val, coef))

    add_element_to_l3(18)
    assert L3 == [13, 15, 12, 17, 15, 18]

    remove_element_from_l3_by_index(1)
    print(L3)

    insert_element_in_l3(20, 0)
    print(L3)

    # fusionnate_two_lists(L1, L4)



main()
