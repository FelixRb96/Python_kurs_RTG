"""
RTG Pythonkurs
@Date: 07.05.2021

Einführung Python Aufgaben
Basics Datentypen, Kontrollstrukturen und Libraries
"""

# Aufgabe 1: 
# 
# a)
# Schreiben sie eine Funktion "add_values" die die Parameter x1 und x2 erhält. 
# Die Funktion soll "x1 + x2" zurückgeben. 
#
# b) 
# Testen sie die oben erstellte funktion mit den Variablen 
x1, x2 = 3, 4
y1, y2 = "Hallo", "RTG"
# Was fällt ihnen dabei auf ? (Denken sie dabei an die Datentypen der Variblen)
# Schreiben sie ihre Beobacktungen als Kommentar in dieses File.

# Aufgabe 2:
# gegeben ist die Folgende Liste:
list_for_exercise = [
        2, 
        3.0, 
        ["This", "might", "be", "a", "list", "in", "a", "list"],
        {
            "can_we_put_random_things_in_lists" : "yes",
            "xyz" : [1,2,3]
            }
        ]

# a) Lassen sie sich per print die Datentypen der Listenelemente ausgeben
# b) printen sie sich aus dem dritten Element von "list_for_exercise" das zweite Element
# c) printen sie sich aus dem vierten Element von "list_for_exercise" das element mit dem key "xyz"

# Aufgabe 3
# a) importieren sie sich die Library "time"
# b) schreiben sie sich eine Funktion "get_time()" die keine Parameter übergeben bekommt, ihnen 
#    die aktuelle Uhrzeit printet und als Rückgabewert ebenfalls die aktuelle Zeit hat. 
#    Finden sie dazu eine angemessene Funktion in der Library "time" (Tipp: verwenden sie "help(time)" nachdem 
#    sie die Library geladen haben).
