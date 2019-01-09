# -*- coding: utf-8 -*-

import random

liczba = random.randint(1, 10)
# print("Wylosowana liczba:", liczba)

for i in range (3):
    print("-"*25)
    print("Próba",i+1)
    odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
    print("Podałeś liczbę: ", odp)
    if liczba==int(odp):
        print("Brawo, zgadles!")
        print("-"*25)
        break
    elif i==2:
        print("Sorry, mialem na mysli liczbę", liczba)
    else:
        print("Pomyłka ...")
        print("-"*25)


