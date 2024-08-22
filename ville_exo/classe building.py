from batiment import Building
from batiment import Immeuble
from batiment import Bank
from batiment import Supermarket

immeuble1 = Immeuble("Fremicourt", 7)
immeuble2 = Immeuble("Commerce", 6)
immeuble3 = Immeuble("Robert Fleury", 6)
immeuble4 = Immeuble("Télégraphe", 5)

supermarket1 = Supermarket("Carrefour", 1, 30000, 20000)
supermarket2 = Supermarket("RapidMarket", 1, 4000, 6000)

bank1 = Bank("Crédit Agricole", 9, 70000000)
bank2 = Bank("Société Générale", 3, 200000)

print("Immeuble:", immeuble1.get_name(), "nb d'étages:", immeuble1.get_floor())
print("Immeuble:", immeuble2.get_name(), "nb d'étages:", immeuble2.get_floor())
print("Immeuble:", immeuble3.get_name(), "nb d'étages:", immeuble3.get_floor())
print("Immeuble:", immeuble4.get_name(), "nb d'étages:", immeuble4.get_floor())
print("Supermarché:", supermarket1.get_name(), "Valeur food en magasin:", supermarket1.get_food(), "Valeur boisson en magasin:", supermarket1.get_drink())
print("Supermarché:", supermarket2.get_name(), "Valeur food en magasin:", supermarket2.get_food(), "Valeur boisson en magasin:", supermarket2.get_drink())
print("Banque:", bank1.get_name(), "nb d'étages:", bank1.get_floor(), "Valeur du coffre:", bank1.get_money())
print("Banque:", bank2.get_name(), "nb d'étages:", bank2.get_floor(), "Valeur du coffre:", bank2.get_money())