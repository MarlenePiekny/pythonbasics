class CalculSurListe():
    def __init__(self, liste):
        self.__liste = liste

    def calculer(self):
        return self._calculer(self.__liste)

    def _calculer(self, liste):
        raise Exception("Not implemented")


