from os import system
import sys
system("cls")

rows = int(input("Entrer le nbr de rows : "))
colmuns = int(input("Entrer le nbr de colnnes : "))
symbols = input("Entrer le symbol utilisée : ")

for i in range(rows):
    for j in range(colmuns):
        print(symbols, end="")
    print()
