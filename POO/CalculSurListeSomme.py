from POO.CalculSurListe import CalculSurListe


class CalculSurListeSomme(CalculSurListe):

    def _calculer(self, numbers):
        sum_result = 0
        for number in numbers:
            sum_result += number
        return sum_result
