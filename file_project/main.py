from enum import Enum


class UserAction(Enum):
    DISPLAY = "afficher"
    ADD = "ajouter"
    QUIT = "quitter"


class UserChoice(Enum):
    NEXT = "s"
    QUIT = "q"


def insert_new_animal_in_zoo():
    new_animal = input("Saisir le nom de l'animal du zoo à ajouter : \n")
    with open("zoo.txt", "a") as zoo_file_to_complete:
        zoo_file_to_complete.write("\n" + new_animal)


def display_animals_of_zoo():
    print("Afficher la liste des nimaux du zoo")
    with open("zoo.txt", "r") as animals_in_zoo:
        user_choice = UserChoice.NEXT.value
        while user_choice == UserChoice.NEXT.value:
            for animal in animals_in_zoo.readlines():
                print(animal)
                user_choice = input("TAPER s - pour suivant OU q - pour quitter\n")
            print("Fin de la liste des animaux du zoo")
            break
        if user_choice == UserChoice.QUIT.value:
            print("Arret du mode affichage")


def manage_zoo(user_action=None):
    while user_action != UserAction.QUIT.value:
        user_action = input("Choisir un mode : ajouter ou afficher\n")
        if user_action == UserAction.ADD.value:
            insert_new_animal_in_zoo()
        if user_action == UserAction.DISPLAY.value:
            display_animals_of_zoo()


def main():

    manage_zoo()


if __name__ == '__main__':
    main()
