import random
import terminaltables
import time

from terminaltables import AsciiTable

table_data = [
    ['Tour', 'Joueur', 'Saisie', 'Resultat', 'Temps'],
    ['1', 'Tarik', '45', 'incorrect', '34']
]
table = AsciiTable(table_data)


def get_secret_price(max_number):
    return random.randint(0, max_number)


game_records = dict()
players = dict()

player_one = str(),
player_two = str(),

levels = { 1 : 50, 2: 100, 3: 1000}


class InvalidInput(Exception):
    """ Inappropriate input type. """
    pass


class AlreadyGivenPrice(Exception):
    """ Already given input. """
    pass


def tour(secret_price, player, tour_number, round_number, already_given_price):
    start_time = time.time()
    user_input = str()
    while not user_input.isdigit() or int(user_input) in already_given_price:
        user_input = input(player + " : Saisir un prix : ")
        try:
            if not user_input.isdigit():
                raise InvalidInput
            if int(user_input) in already_given_price:
                raise AlreadyGivenPrice
        except InvalidInput:
            print("Vous n'avez pas saisi un nombre")
            pass
        except AlreadyGivenPrice:
            print("Ce prix a déjà été donné ")
            pass

    user_input = int(user_input)
    end_time = time.time()
    if user_input == secret_price:
        game_records[str(round_number) + "-" + str(tour_number) + player] = \
            [player, round(end_time - start_time), "correct", user_input]
        print("Bravo")
        return True
    else:
        if user_input not in already_given_price:
            already_given_price.append(user_input)
        # [already_given_price.append(user_input) for input_already_given in already_given_price
        #  if (user_input not in input_already_given)]

        game_records[str(round_number) + "-" + str(tour_number) + player] = \
            [player, round(end_time - start_time), "incorrect", user_input]
        print("Ce n'est pas le juste prix")
        print(already_given_price)
        return False


def playing_round(round_number, given_level):
    secret_price = None
    for level, max_price in levels.items():
        if given_level == level:
            secret_price = get_secret_price(max_price)
            print("Vous avez choisi le mode", level, "le juste prix est en dessous de", max_price, "€")
    already_given_price = list()
    print(secret_price)

    is_secret_price_found = False

    for i in range(1, 10):
        if not is_secret_price_found:
            if i % 2 != 0:
                is_secret_price_found = tour(secret_price, players['player_one'], i, round_number, already_given_price)
            else:
                is_secret_price_found = tour(secret_price, players['player_two'], i, round_number, already_given_price)
        else:
            break


def play():
    players['player_one'] = input("Saisir le nom du joueur 1 : ")
    players['player_two'] = input("Saisir le nom du joueur 2 : ")

    input_level = int(input("Choisir une niveau 1-facile, 2-normal, 3-hard"))

    for i in range(1, 6):
        print("Round : ", i)
        playing_round(i, input_level)


def main():
    start = time.time()
    end = time.time()
    print(end - start)
    print(table.table)
    play()
    print(game_records)


if __name__ == '__main__':
    main()
