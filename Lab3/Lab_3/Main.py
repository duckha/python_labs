import operator


class Currencies:
    def __init__(self, type):
        self.type = type
        if type == 'dollar':
            self.currenciesForWeek = {'monday': 63.52, 'tuesday': 63.12, 'wednesday': 63.91, 'thursday': 64.02,
                                      'friday': 63.12, 'saturday': 63.72, 'sunday': 64.04}
        if type == "euro":
            self.currenciesForWeek = {'monday': 70.82, 'tuesday': 69.62, 'wednesday': 69.31, 'thursday': 70.22,
                                      'friday': 69.02, 'saturday': 69.12, 'sunday': 70.54}

    def printMostProfitable(self):
        sorted_currencies = sorted(self.currenciesForWeek.items(), key=operator.itemgetter(1))
        print(f"The most profitable day for {self.type} is {sorted_currencies[0][0]}")


dollarFirst = Currencies(type="dollar")
dollarFirst.printMostProfitable()
euroSecond = Currencies(type="euro")
euroSecond.printMostProfitable()
