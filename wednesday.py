x=chr(5000)

from os import system
from time import sleep

clear= lambda : system("clear")
for i in range(10):
    print(" "* i, x)
    clear()