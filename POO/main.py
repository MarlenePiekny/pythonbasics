from POO.CalculSurListeSomme import CalculSurListeSomme
from POO.CalculSurListeProduit import CalculSurListeProduit
from POO.CalculSurListe import CalculSurListe


if __name__ == '__main__':
    # c = CalculSurListe([1, 2, 3, 4])
    # print(c.calculer())
    c = CalculSurListeSomme([1, 2, 3, 4])
    print(c.calculer())
    c = CalculSurListeProduit([1, 2, 3, 4])
    print(c.calculer())
    c = CalculSurListeProduit([2])
    print(c.calculer())
