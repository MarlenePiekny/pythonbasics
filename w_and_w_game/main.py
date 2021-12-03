class Character:
    def __init__(self, life_level, physical_attack, magical_attack, physical_shield, magical_shield):
        self._life_level = life_level
        self._physical_attack = physical_attack
        self._magical_attack = magical_attack
        self._physical_shield = physical_shield
        self._magical_shield = magical_shield


class Wizard(Character):
    def __init__(self):
        super().__init__(self, 50, 10, 20, 5, 10)


class Archer(Character):
    def __init__(self):
        super().__init__(self, 50, 10, 20, 5, 10)


def play():
    wizard = Wizard()


def main():
    play()


if __name__ == '__main__':
    main()
