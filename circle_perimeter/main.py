# This script calculate circle perimeter according to its radius

import math


def circle_perimeter(radius):
    """Calaculate circle perimetre from its radius.
    :param radius: circle radius
    :return circle perimeter

    """
    return 2 * math.pi * radius


def main():
    """Main programm"""
    # ask for radius to the user
    user_input = input("Quel est le rayon du cercle (en cm)?")
    radius = float(user_input)

    # calculate perimeter
    perimeter = circle_perimeter(radius)

    # display perimeter to the user
    print("Le périmètre d'un cercle de rayon", radius, "est", perimeter, "cm")


if __name__ == "__main__":
    main()
