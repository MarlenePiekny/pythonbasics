# This script aims to simulate the right price game


from random import randint

MIN_WINNING_GAME = 2


def chose_random_int() -> int:
    return randint(0, 100)


def tour() -> bool:
    the_right_price = chose_random_int()
    print(the_right_price)

    user_remaining_tries = 10
    user_input = -1

    while user_remaining_tries > 0 and user_input != the_right_price:

        try:
            user_input = int(input("Trouve le juste prix entre 0 et 100 euros :\n"))
        except ValueError:
            print("La donnée saisie :", user_input, "n'est pas un nombre,"
                                                    "\nVeuillez saisir un nombre. Exemple du format : 3, 85, 42")
        else:
            user_remaining_tries -= 1
            print("Dommage! ce n'est pas le juste prix"
                  "\nEssaie encore, il te reste", user_remaining_tries, "tentative(s)")

    if user_input == the_right_price:
        print("Bravo! Le juste prix est bien", the_right_price)
        return True;
    else:
        print("Perdu! Le juste prix n'est pas", user_input, "et tu n'as plus de tentative",
              "\nLe juste prix était", the_right_price)
        return False;


def main():
    print("Bienvenue au jeu du juste prix")

    user_games = 3
    user_winning_game = 0

    for i in range(user_games):
        if tour():
            user_winning_game += 1
        user_games -= 1
        print("Il te reste", user_games, "parties à jouer")

    if user_winning_game < MIN_WINNING_GAME:
        print("Vous avez perdu")
    else:
        print("Vous avez gagné")


main()
