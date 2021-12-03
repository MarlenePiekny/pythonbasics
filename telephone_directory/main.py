from enum import Enum

numbers = [18, 15, 14, 13, 19]
telephone_directory = {"Greg": "0138925447", "Mati": "0632548759", "Steve": "0215875465", "Alexis": "0454878565"}


class DirectoryAction(Enum):
    LIST = 'L'
    ADD = 'A'
    DELETE = 'S'


def sort_numbers_list(direction=True):
    numbers.sort() if direction else numbers.sort(reverse=True)


# def get_phone_numbers_of_people_name_starting_with(letter='A'):
#     phone_numbers = []
#     for name, phone_number in telephone_directory.items():
#         if name[0] == letter:
#             phone_numbers.append(phone_number)
#             return phone_numbers
#     return ""

def get_phone_numbers_of_people_name_starting_with(letter='A'):
    return [phone_number for name, phone_number in telephone_directory.items() if (name[0] == letter)]


def list_contacts_in_telephone_directory():
    return telephone_directory.copy()


def add_contact_to_telephone_directory(name, phone_number):
    if name not in telephone_directory:
        telephone_directory[name] = phone_number
    else:
        print("ce nom existe déjà dans le répertoire")


def delete_contact_by_name_in_telephone_directory(name):
    if name in telephone_directory:
        del telephone_directory[name]


def display_telephone_directory(telephone_directory: dict):
    print("Voici vos contacts : ")
    for name, phone_number in telephone_directory.items():
        print(name, ":", phone_number)


def ask_for_contact_to_add():
    return {input("Nom du nouveau contact : "): input("Numéro du nouveau contact : ")}


def ask_for_contact_name_to_delete():
    return input("Saisir le nom du contact à supprimer : ")


def user_action_list():
    display_telephone_directory(list_contacts_in_telephone_directory())


def user_action_add():
    new_contact = ask_for_contact_to_add()
    add_contact_to_telephone_directory(new_contact.keys, new_contact.values)
    print("Le contact", new_contact.keys, " : ", new_contact.values(), "a bien été ajouté")


def user_action_delete():
    contact_name_to_delete = ask_for_contact_name_to_delete()
    delete_contact_by_name_in_telephone_directory(contact_name_to_delete)
    print("Le contact", contact_name_to_delete, "a bien été supprimé")


def play_telephone_directory():
    input_action = input("Choisir une action parmi: \nL - lister \nA - Ajouter \nS - Supprimer\nVotre choix : ")

    if input_action not in [DirectoryAction.LIST.value, DirectoryAction.ADD.value, DirectoryAction.DELETE.value]:
        print("Ceci n'est pas une action de la liste")
    else:
        if input_action == DirectoryAction.LIST.value:
            user_action_list()
        if input_action == DirectoryAction.ADD.value:
            user_action_add()
        if input_action == DirectoryAction.DELETE.value:
            user_action_delete()


def main():
    sort_numbers_list()
    assert numbers == [13, 14, 15, 18, 19]

    sort_numbers_list(False)
    assert numbers == [19, 18, 15, 14, 13]

    phone_number_of_people_name_starting_with_g = get_phone_numbers_of_people_name_starting_with('G')
    assert phone_number_of_people_name_starting_with_g == ["0138925447"]
    phone_number_of_people_name_by_default = get_phone_numbers_of_people_name_starting_with()
    assert phone_number_of_people_name_by_default == ["0454878565"]

    list_all_contacts = list_contacts_in_telephone_directory()
    assert list_all_contacts == \
           {"Greg": "0138925447", "Mati": "0632548759", "Steve": "0215875465", "Alexis": "0454878565"}

    add_contact_to_telephone_directory("Karl", "0565847525")
    assert telephone_directory["Karl"] == "0565847525"

    delete_contact_by_name_in_telephone_directory("Greg")
    assert telephone_directory == {"Mati": "0632548759", "Steve": "0215875465", "Alexis": "0454878565",
                                   "Karl": "0565847525"}

    play_telephone_directory()


if __name__ == '__main__':
    main()
