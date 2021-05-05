"""
RTG Pythonkurs
@Date: 07.05.2021

Einführung Python Aufgaben
Basics Datentypen, Kontrollstrukturen und Libraries
"""

# Aufgabe 1: 
# 
# a)
# Schreiben Sie eine Funktion "add_values" die die Parameter x1 und x2 erhält. 
# Die Funktion soll "x1 + x2" zurückgeben. 
def add_values(x1, x2):
    """
    Adds two objects together, if they have a well defined __add__ method implemented

    @params:
        x1: object with a dunder method __add__
        x2: object that can be passed to the dunder method __add__ of x1
    
    @returns:
        object, that is just the result of x1.__add__(x2)
    """
    return x1 + x2

# b) 
# Testen Sie die oben erstellte Funktion mit den Variablen:
x1, x2 = 3, 4
y1, y2 = "Hallo", "RTG"
# Was fällt auf? (Denken sie dabei an die Datentypen der Variblen)
# Schreiben sie ihre Beobacktungen als Kommentar in dieses File.

# Im verleich zu C ist der Funktion egal welche Datentypen übergeben werden. 
# Dieses Prinzip heißt Polymorphie des "+" Operators
add_values(x1, x2)
add_values(y1, y2)

# Aufgabe 2:
# Es sei die folgende Liste gegeben:
list_for_exercise = [
        2, 
        3.0, 
        ["This", "might", "be", "a", "list", "in", "a", "list"],
        {
            "can_we_put_random_things_in_lists" : "yes",
            "xyz" : [1,2,3]
            }
        ]

# a) Lassen Sie sich per print die Datentypen der Listenelemente ausgeben.
for elem in list_for_exercise:
    print(elem)

# b) Printen Sie sich aus dem dritten Element von "list_for_exercise" das zweite Element.
print(list_for_exercise[2][1])

# c) Printen sie sich aus dem vierten Element von "list_for_exercise" das Element mit dem key "xyz".
print(list_for_exercise[3]['xyz'])

# Aufgabe 3
# a) Importieren Sie die Library "time".
import time

# b) Schreiben Sie sich eine Funktion "get_time()" die keine Parameter übergeben bekommt,
#    die aktuelle Uhrzeit printet und als Rückgabewert ebenfalls die aktuelle Zeit hat. 
#    Finden Sie dazu eine angemessene Funktion in der Library "time" (Tipp: verwenden Sie "help(time)" nachdem 
#    sie die Library geladen haben).
def get_time():
    """ returns the current time given by a system call to the os."""
    result = time.localtime()
    timestring = f"{result.tm_hour} h {result.tm_min} min {result.tm_sec} sec"
    print(timestring)
    return timestring
