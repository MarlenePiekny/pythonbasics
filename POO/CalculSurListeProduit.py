from POO.CalculSurListe import CalculSurListe


class CalculSurListeProduit(CalculSurListe):

    def _calculer(self, numbers):
        product_result = 1
        for number in numbers:
            product_result *= number
        return product_result
