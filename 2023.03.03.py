class Employee:
    _name: str
    _salary: float
    def __init__(self, name: str) -> None:
        self._name = name
        self._salary = 100.0
    def CalculateSalary(self) -> float:
        return self._salary
class Cook(Employee):
    _isWorking: bool
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._salary = 150.0
class Waiter(Employee):
    _tips: float
    def __init__(self, name) -> None:
        super().__init__(name)
        self._salary = 135.0
        self._tips = 0.0
    def CalculateSalary(self) -> float:
        return super().CalculateSalary()+self._tips
class Restorans:
    _employees: 'list[Employee]' # Pēdiņās liek: Sarakstus, vārdnīcas utt.
                                 # Tā pat pēdiņās liek klases kuras ir definētas vēlāk
                                 # Piemēram, ja klase izmanto citu klasi, un tā klase izmanto 
                                 # šo klasi. Tad ieliek pēdiņās, lai pateiktu Python, ka klase
                                 # ir definēta kaut kur vēlāk.
    def __init__(self, employees: 'list[Employee]') -> None:
        self._employees = employees
class WhiteGood:
    _name: str
class Ingredient:
    _name: str
    _cost: float
    _uses: WhiteGood
class Recipe:
    _ingredients: 'dict' # sastāvdaļa: skaits
    _secondsToCook: int
class Order:
    _order: 'list[Recipe]'
class Customer:
    _availableMoney: float
class Kitchen: 
    _cooks: 'list[Cook]'
    _availableIngredients: 'list[Ingredient]'
    _whiteGoods: 'list[WhiteGood]'
    def Cook(self, cook: Cook, recipe: Recipe):
        cook._isWorking = True
        for ingredient in recipe._ingredients:
            isIngredientAvailable = False
            for availableIngredient in self._availableIngredients:
                if availableIngredient._name == ingredient: # Te ir jāsaprot kā ingredient piekļūt no receptes.
                    isIngredientAvailable
               
class Food:
    _ingredients: 'list[Ingredient]'


Janis = Waiter("Janis")
Emils = Cook("Emils")
Restorans = Restorans([Janis, Emils])
for employee in Restorans._employees:
    print(employee._name)
    print(type(employee))
