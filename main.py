class Fractie:
    def __init__(self, numitor, numarator):
        self.__numarator = numarator
        self.__numitor = numitor

    def __str__(self):
        return f"({self.__numarator}/{self.__numitor})"

    def __add__(self, other):
        fractie1 = other.__numitor * self.__numarator / self.__numitor
        fractie2 = self.__numitor * other.__numarator / self.__numitor

        return fractie1 + fractie2

    def __sub__(self, other):
        fractie1 = other.__numitor * self.__numarator / self.__numitor
        fractie2 = self.__numitor * other.__numarator / self.__numitor

        return fractie1 - fractie2

    def inverse(self):
        return self.__numitor/self.__numarator

