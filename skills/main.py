L1 = [1, 1, 1, 1, 1]
L3 = [13, 15, 12, 17, 15]
L4 = [18, 15, 14, 13, 19, 20]

D1 = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
D2 = {"Dupont": [13, 12, 9], "Hervy": [18, 12, 10], "Geoffroy": [17, 18, 9], "Layec": [11, 10, 9]}


def add_element_to_l3(element):
    L3.append(element)


def remove_element_from_l3_by_index(index):
    del L3[index]


def insert_element_in_l3(element, index):
    L3.insert(index, element)


def merge_two_lists(first_list, second_list):
    first_list.extend(second_list)


def retrieve_cut_l1_until_third_element():
    return L1[:3]


def create_list_from_copy(base_list):
    return base_list.copy()


def cut_second_element_from_l4():
    return L4.pop(1)


def display_list(elements):
    for element in elements:
        print(element)


def create_empty_dict():
    return dict()


def add_item_to_dictionary(dictionary: dict, key, value):
    dictionary[key] = value


def display_dictionary_element_value_from_key(dictionary: dict, key):
    return dictionary[key]


def edit_element_from_its_key(dictionary: dict, key, value):
    dictionary[key] = value


def delete_element_by_key(dictionary: dict, key):
    del dictionary[key]


def is_element_find_by_key_in_dict(dictionary: dict, key):
    return key in dictionary


def display_dictionary(dictionary: dict):
    for name, grades in dictionary.items():
        print(name, "a eu les notes", grades)


def main():
    add_element_to_l3(18)
    assert L3 == [13, 15, 12, 17, 15, 18]

    remove_element_from_l3_by_index(0)
    assert L3 == [15, 12, 17, 15, 18]

    insert_element_in_l3(20, 1)
    assert L3 == [15, 20, 12, 17, 15, 18]

    merge_two_lists(L1, L4)
    assert L1 == [1, 1, 1, 1, 1, 18, 15, 14, 13, 19, 20]

    cut_list = retrieve_cut_l1_until_third_element()
    assert cut_list == [1, 1, 1]

    created_list = create_list_from_copy(L4)
    assert created_list == [18, 15, 14, 13, 19, 20]
    assert L4 == [18, 15, 14, 13, 19, 20]

    element = cut_second_element_from_l4()
    assert element == 15
    assert L4 == [18, 14, 13, 19, 20]

    display_list(L4)

    new_dict = create_empty_dict()
    assert new_dict == {}

    add_item_to_dictionary(new_dict, 1, "easy")
    add_item_to_dictionary(new_dict, 1, "normal")
    # assert new_dict == {1: "easy"}
    assert new_dict == {1: "normal"}

    element_given_its_key = display_dictionary_element_value_from_key(D2, "Dupont")
    assert element_given_its_key == [13, 12, 9]

    edit_element_from_its_key(D2, "Geoffroy", [0, 0, 0])
    assert D2["Geoffroy"] == [0, 0, 0]

    delete_element_by_key(D2, "Hervy")
    assert D2 == {"Dupont": [13, 12, 9], "Geoffroy": [0, 0, 0], "Layec": [11, 10, 9]}

    assert is_element_find_by_key_in_dict(D1, "Dupont")

    display_dictionary(D2)


if __name__ == '__main__':
    main()
