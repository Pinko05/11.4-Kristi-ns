class Maja:
    dzivokli = [] #Dzivoklis
    
    def _init_(self):
        pirmais= Dzivoklis()
        self.dzivokli.append(pirmais)

    def IegutAugstumu(self):
        augstums = 5
        for dzivoklis in self.dzivokli:
            augstums += dzivoklis.IegutAugstumu()
        print(augstums)

class Dzivoklis:
    augstums = 0
    def IegutAugstumy(self):
        return self.augstums

maja = Maja()
maja.dzivokli

class Ekrans:
    izmers: int
class Dators:
    ekrans:Ekrans
    def IegutEkranaIzmeru(self):
        self.ekrans.izmers